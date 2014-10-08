#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Documentação em: http://pyalsaaudio.sourceforge.net/libalsaaudio.html

import alsaaudio

print('ALSA Audio')

print('\nPlacas disponíveis:')

for x in alsaaudio.cards():
    print(x)

print('\nControles disponíveis:')

for x in alsaaudio.mixers():
    print(x)

mixer = alsaaudio.Mixer(control='Master', id=0, cardindex=0)

print('\nO volume de playback do controle Master é: %s' % mixer.getvolume('playback'))
print('O volume do captura controle Master é: %s' % mixer.getvolume('capture'))
print('Controle Master está mudo.' if mixer.getmute() == 1 else 'Controle Master não está mudo.')

mixer.setvolume(100L)

print('O volumedo do controle Master foi alterado para 100.')

mixer = alsaaudio.Mixer(control='Mic', id=0, cardindex=0)

print('\nO volume de playback do controle Mic é: %s' % mixer.getvolume('playback'))
print('O volume do captura controle Mic é: %s' % mixer.getvolume('capture'))
print('Controle Mic está mudo.' if mixer.getmute() == 1 else 'Controle Mic não está mudo.')

mixer.setvolume(100L)

print('O volumedo do controle Mic foi alterado para 100.')

mixer = alsaaudio.Mixer(control='Capture', id=0, cardindex=0)

mixer.setrec(False)
print('Captura desabilitada no controle Capture')

mixer.setrec(True)
print('Captura habilitada no controle Capture')