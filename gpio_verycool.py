import RPi.GPIO as GPIO
from time import sleep
from Instruments import *
##import Piano_Chord_Recognition as PCR
from Piano_Chord_Recognition import bigFunk

GPIO.setmode(GPIO.BCM)

keys = [18, 19, 20, 21, 22, 23, 24, 25, 26, 17, 16, 13]
down = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

my_list = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
##my_list = ['C', 'E', 'G', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

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
chord = False
print("Start")
try:
    while (True):
        # play a note when pressed...until released
        """key = wait_for_note_start()
        
        print(key)
        piano.playNote(key)
        # if the play button was pressed
        wait_for_note_stop(key)"""
        for i in range(len(keys)):
            if (GPIO.input(keys[i]) and down[i] == 0):
                down[i] = 1
                piano.playNote(i)
            elif (not GPIO.input(keys[i]) and down[i] == 1):
                down[i] = 0
        num = 0
        for push in down:
            if (push == 1):
                num += 1
                
        if (num == 3 and chord == False):
            temp = []
            relist = []
            for push in range(len(down)):
                if down[push] == 1:
                    temp.append(my_list[push])
##          PCR.chordReader('A', 'C', 'E', PCR.final_list)
            bigFunk(temp[0], temp[1], temp[2])
            chord = True
            print(temp)
        elif (num != 3):
            chord = False
            #print(chord)
        
        
except KeyboardInterrupt:
    print("KeyboardInterrupt")
    # reset the GPIO pins
    GPIO.cleanup()
print("something broke")
