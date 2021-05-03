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
            piano.press_down(0)
        if (is_pressed("w")):
            piano.press_down(1)
        if (is_pressed("e")):
            piano.press_down(2)
        if (is_pressed("r")):
            piano.press_down(3)
        if (is_pressed("t")):
            piano.press_down(4)
        if (is_pressed("y")):
            piano.press_down(5)
        if (is_pressed("u")):
            piano.press_down(6)
        if (is_pressed("i")):
            piano.press_down(7)
        if (is_pressed("o")):
            piano.press_down(8)
        if (is_pressed("p")):
            piano.press_down(9)
        if (is_pressed("[")):
            piano.press_down(10)
        if (is_pressed("]")):
            piano.press_down(11)

    except KeyboardInterrupt:
        break

