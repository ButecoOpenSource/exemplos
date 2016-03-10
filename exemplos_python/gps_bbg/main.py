# -*- coding: utf-8 -*-

from bottle import route, run, template

import gps


@route('/')
def index():
    pos = gps.get_current_position()

    if pos:
        return template('index', api_key='<GOOGLE MAPS KEY>', latitude=pos.latitude, longitude=pos.longitude)
    else:
        return template('error')


if __name__ == '__main__':
    gps.start()
    run(host='0.0.0.0', port=8081)
