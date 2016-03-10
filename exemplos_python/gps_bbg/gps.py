# -*- coding: utf-8 -*-

import Adafruit_BBIO.UART as UART
import serial
import thread
import Queue
import nmea

from collections import namedtuple

Pos = namedtuple('Pos', ['latitude', 'longitude'])

q = Queue.Queue()
parser = nmea.NMEAParser()


def listen(q):
    UART.setup("UART2")

    with serial.Serial(port="/dev/ttyO2", baudrate=9600) as ser:
        print('Connected to GPS: %s' % ser.name)
        while True:
            sentence = ser.readline()
            # remove \r\n
            sentence = sentence[:-2]

            if sentence[0] == '$':
                try:
                    gps_data = parser.parse(sentence)

                    if gps_data.is_valid and gps_data.sentence_name != 'VTG':
                        q.put(gps_data)
                except:
                    pass


def start():
    thread.start_new_thread(listen, (q,))


def get_current_position(wait=False):
    try:
        gps_data = q.get(wait)
        return Pos(latitude=gps_data.latitude_degree, longitude=gps_data.longitude_degree)
    except:
        return None


if __name__ == '__main__':
    start()

    while True:
        print(get_current_position(True))
