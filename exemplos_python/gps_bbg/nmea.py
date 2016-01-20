# -*- coding: utf-8 -*-
#
# NMEA 0183 2.3 Parser implementation
#
# This module implements only GGA, GLL, RMC and VTG sentences.
#
# NMEA 0183 Protocol Reference
# http://www.tronico.fi/OH6NT/docs/NMEA0183.pdf
#

import re

from datetime import date, time


class ParseException(Exception):
    pass


class UTCTimeParser(object):
    '''
        Convert string UTC Time into datetime.time.
        It must follow the format hhmmss (161229) or hhmmss.sss (161229.487).
    '''

    def __new__(cls, value):
        try:
            h, m, s, _, ms = re.match(r'^(\d{2})(\d{2})(\d{2})(\.(\d+))?$', value).groups()
            ms = ms or 0
            return time(int(h), int(m), int(s), int(ms))
        except:
            raise ParseException('Can\'t parse value into UTC Time: %s' % value)


class DateParser(object):
    '''
        Convert string Date into datetime.date.
        It must follow the format ddmmyy (010115).
    '''

    def __new__(cls, value):
        try:
            d, m, y = re.match(r'^(\d{2})(\d{2})(\d{2})$', value).groups()
            y = '20%s' % y
            return date(int(y), int(m), int(d))
        except:
            raise ParseException(
                'Can\'t parse value into Date: %s' % value)


class Sentence(object):
    sentence_name = 'Unknown'
    sentence_description = 'Unknown Sentence'
    fields = ()

    def __init__(self):
        self._fields_count = len(self.fields)
        self._last = self._fields_count - 1

    def parse(self, data):
        data = str(data)
        sentence, checksum = data.split('*')
        raw_fields = sentence.split(',')

        if len(raw_fields) != self._fields_count:
            raise ParseException(
                'Field count mismatch. Expected %d fields, but found %d.' % (self._fields_count, len(raw_fields)))

        for index, field in enumerate(self.fields):
            field_name, _, field_type = field
            try:
                value = raw_fields[index]
                value = value.strip()

                if value:
                    setattr(self, field_name, field_type(value))
                else:
                    setattr(self, field_name, None)
            except:
                raise ParseException(
                    'Can\'t parse value into field "%s": %s' % (field_name, value))

        return self

    @property
    def is_valid(self):
        return False

    def __repr__(self):
        return '%sSentence(is_valid=%s)' % (self.sentence_name, self.is_valid)


class LatLonMixin:

    def _convert(self, value):
        '''
        Convert Latitude/Longitude NMEA format to Python float degree.

        Args:
            value: ddmm.mmmm
        '''
        if not value:
            return 0.0

        d, m = re.match(r'^(\d+)(\d\d\.\d+)$', value).groups()
        return float(d) + float(m) / 60

    @property
    def latitude_degree(self):
        lat = self._convert(self.latitude)

        if self.ns_indicator == 'S':
            return abs(lat) * -1

        return abs(lat)

    @property
    def longitude_degree(self):
        lon = self._convert(self.longitude)

        if self.ew_indicator == 'W':
            return abs(lon) * -1

        return abs(lon)


class KnotToKmHMixin:

    @property
    def speed_km_h(self):
        return self.speed_over_ground * 1.852


class GGASentence(Sentence, LatLonMixin):
    sentence_name = 'GGA'
    sentence_description = 'Global Positioning System Fix Data'
    fields = (
        ('utc_time', 'UTC Time', UTCTimeParser),
        ('latitude', 'Latitude', str),
        ('ns_indicator', 'N/S Indicator', str.upper),
        ('longitude', 'Longitude', str),
        ('ew_indicator', 'E/W Indicator', str.upper),
        ('fix_quality', 'Position Fix Indicator', int),
        ('num_satellites', 'Satellites Used', int),
        ('hdop', 'Horizontal Dilution of Precision', float),
        ('msl_altitude', 'MSL Altitude', float),
        ('msl_units', 'MSL Altitude Units', str),
        ('geoid_separation', 'Geoid Separation', float),
        ('geoid_sep_units', 'Geoid Separation Units', str),
        ('age_diff', 'Age of Differential GPS data', float),
        ('station_id', 'Differential reference station ID', str),
    )

    @property
    def is_valid(self):
        return self.fix_quality in [1, 2]


class GLLSentence(Sentence, LatLonMixin):
    sentence_name = 'GLL'
    sentence_description = 'Geographic Position – Latitude/Longitude'
    fields = (
        ('latitude', 'Latitude', str),
        ('ns_indicator', 'N/S Indicator', str.upper),
        ('longitude', 'Longitude', str),
        ('ew_indicator', 'E/W Indicator', str.upper),
        ('utc_time', 'UTC Time', UTCTimeParser),
        ('status', 'Status', str.upper),
        # ('mode', 'Mode', str), NMEA V 3.00
    )

    @property
    def is_valid(self):
        return self.status == 'A'


class RMCSentence(Sentence, LatLonMixin, KnotToKmHMixin):
    sentence_name = 'RMC'
    sentence_description = 'Recommended Minimum Specific GNSS Data'
    fields = (
        ('utc_time', 'UTC Time', UTCTimeParser),
        ('status', 'Status', str.upper),
        ('latitude', 'Latitude', str),
        ('ns_indicator', 'N/S Indicator', str.upper),
        ('longitude', 'Longitude', str),
        ('ew_indicator', 'E/W Indicator', str.upper),
        ('speed_over_ground', 'Speed Over Ground (knots)', float),
        ('course_over_ground', 'Course Over Ground (degrees)', float),
        ('data', 'Date', DateParser),
        ('magnetic_variation', 'Magnetic variation', str.upper),
        ('mv_ew_indicator', 'E/W Indicator', str.upper),
        ('mode', 'Mode', str),
    )

    @property
    def is_valid(self):
        return self.status == 'A'


class VTGSentence(Sentence):
    sentence_name = 'VTG'
    sentence_description = 'Course Over Ground and Ground Speed'
    fields = (
        ('course_1', 'Measured heading', float),
        ('reference_1', 'Reference', str),
        ('course_1', 'Measured heading', float),
        ('reference_2', 'Reference', str),
        ('speed_1', 'Speed over ground in knots', float),
        ('units_1', 'Units', str),
        ('speed_2', 'Speed over ground in kilometers/hour', float),
        ('units_2', 'Units', str),
        # ('mode', 'Mode', str), NMEA V 3.00
    )

    @property
    def is_valid(self):
        return True


class NMEAParser(object):
    parsers = {
        GGASentence.sentence_name: GGASentence,
        GLLSentence.sentence_name: GLLSentence,
        RMCSentence.sentence_name: RMCSentence,
        VTGSentence.sentence_name: VTGSentence,
    }

    def _get_parser(self, name):
        parser = NMEAParser.parsers.get(name.upper())

        if parser:
            return parser()

        return None

    def parse(self, data):
        if not data:
            raise ParseException('Can\'t parse empty data.')

        if data[0] == u'$':
            data = data[1:]

        if data[0:2] == u'GP':
            data = data[2:]

        sentence = data[0:3]
        parser = self._get_parser(sentence)

        if not parser:
            raise ParseException('Can\'t find parser for sentence: %s' % sentence)

        return parser.parse(data[4:])

if __name__ == '__main__':
    parser = NMEAParser()
    print(parser.parse('$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47'))
    print(parser.parse('$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D'))
    print(parser.parse('$GPGGA,161229.487,3723.2475,N,12158.3416,W,1,07,1.0,9.0,M, , , ,0000*18'))
    print(parser.parse('$GPGLL,3723.2475,N,12158.3416,W,161229.487,A*41'))
    print(parser.parse('$GPVTG,309.62,T, ,M,0.13,N,0.2,K*23'))
    print(parser.parse('$GPRMC,161229.487,A,3723.2475,N,12158.3416,W,0.13,309.62,120508,,,A*10'))
    print(parser.parse('$GPGGA,234803.979,,,,,0,6,,,M,,M,,*47'))
    print(parser.parse('$GPRMC,234840.953,V,,,,,0.00,0.00,031115,,,N*4C'))
