# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import sys

from collections import namedtuple

Auth = namedtuple('Auth', ['user', 'pwd'])

MQTT_ADDRESS = '127.0.0.1'
# descomente esta linha para usar o servidor da Fundação Eclipse.
# MQTT_ADDRESS = 'iot.eclipse.org'
MQTT_PORT = 1883
# descomente esta linha caso seu servidor possua autenticação.
# MQTT_AUTH = Auth('login', 'senha')
MQTT_TIMEOUT = 60

if sys.version_info[0] == 3:
    input_func = input
else:
    input_func = raw_input


def on_connect(client, userdata, flags, rc):
    print('Conectado. Resultado: %s' % str(rc))
    result, mid = client.subscribe('/buteco/topico')
    print('Inscrevendo-se no tópico "/buteco/topico" (%d)' % mid)


def on_subscribe(client, userdata, mid, granted_qos):
    print('Inscrito no tópico: %d' % mid)


def on_message(client, userdata, msg):
    print('Mensagem recebida no tópico: %s' % msg.topic)

    if msg.topic == '/buteco/topico':
        print('Conteúdo da mensagem: %s' % msg.payload)
    else:
        print('Tópico desconhecido.')


def loop():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    # descomente esta linha caso seu servidor possua autenticação.
    # client.username_pw_set(MQTT_AUTH.user, MQTT_AUTH.pwd)
    client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)
    client.loop_forever()


def send_message(msg):
    client = mqtt.Client()
    # descomente esta linha caso seu servidor possua autenticação.
    # client.username_pw_set(MQTT_AUTH.user, MQTT_AUTH.pwd)
    client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)
    result, mid = client.publish('/buteco/topico', msg)
    print('Mensagem enviada ao canal: %d' % mid)


if __name__ == '__main__':
    if '--serve' in sys.argv:
        loop()
    elif '--send' in sys.argv:
        msg = input_func('Digite uma mensagem:\n')
        send_message(msg)
