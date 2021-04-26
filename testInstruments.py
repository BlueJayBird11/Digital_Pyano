import Instruments
from keyboard import is_pressed #pip3 install keyboard

import pyaudio
import math

wave = Instruments.Wave()
piano = Instruments.Piano()
while (True):
    try:
        if (is_pressed("a")):
            wave.testSound()
        
        if (is_pressed("q")):
            piano.playNote(0)
        if (is_pressed("w")):
            piano.playNote(1)
        if (is_pressed("e")):
            piano.playNote(2)
        if (is_pressed("r")):
            piano.playNote(3)
        if (is_pressed("t")):
            piano.playNote(4)
        if (is_pressed("y")):
            piano.playNote(5)
        if (is_pressed("u")):
            piano.playNote(6)
        if (is_pressed("i")):
            piano.playNote(7)
        if (is_pressed("o")):
            piano.playNote(8)
        if (is_pressed("p")):
            piano.playNote(9)
        if (is_pressed("[")):
            piano.playNote(10)
        if (is_pressed("]")):
            piano.playNote(11)
    except KeyboardInterrupt:
        break

