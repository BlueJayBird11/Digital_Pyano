import RPi.GPIO as GPIO
from time import sleep
from Instruments import *


GPIO.setmode(GPIO.BCM)

keys = [18, 19, 20, 21, 22]
GPIO.setup(keys, GPIO.IN, GPIO.PUD_DOWN)

piano = Piano()

def wait_for_note_start():
    while True:
        for key in range(len(keys)):
            if (GPIO.input(keys[key])):
                return key
        sleep(0.01)

def wait_for_note_stop(key):
    while GPIO.input(keys[key]):
        sleep(0.1)

print("Start")
try:
    while (True):
        # play a note when pressed...until released
        key = wait_for_note_start()
        
        print(key)
        piano.playNote(key)
        # if the play button was pressed
        wait_for_note_stop(key)
        
except KeyboardInterrupt:
    # reset the GPIO pins
    GPIO.cleanup()
