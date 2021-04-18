import Instrument
from keyboard import is_pressed #pip3 install keyboard

import pyaudio
import math

wave = Instrument.Wave()


print(wave.getF(11))

def playSinWAVE(self, FREQUENCY = 261.63):
        #generating waves
        PyAudio = pyaudio.PyAudio     #initialize pyaudio
        BITRATE = 5000     #number of frames per second/frameset.
        FREQUENCY = 261.63     #Hz, waves per second, 261.63=C4-note.
        LENGTH = 0.01    #seconds to play sound

        if FREQUENCY > BITRATE:
            BITRATE = FREQUENCY+100
        NUMBEROFFRAMES = int(BITRATE * LENGTH)
        RESTFRAMES = NUMBEROFFRAMES % BITRATE

        WAVEDATA = ''
        for x in range(NUMBEROFFRAMES):
            WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))
        for x in range(RESTFRAMES):
            WAVEDATA = WAVEDATA+chr(128)
        
        p = PyAudio()
        stream = p.open(format = p.get_format_from_width(1),channels = 2,rate = BITRATE,output = True)
        stream.write(WAVEDATA)
        stream.stop_stream()
        stream.close()
        p.terminate()


PyAudio = pyaudio.PyAudio     #initialize pyaudio
BITRATE = 5000     #number of frames per second/frameset.
FREQUENCY = 261.63     #Hz, waves per second, 261.63=C4-note.
LENGTH = 0.5    #seconds to play sound

if FREQUENCY > BITRATE:
    BITRATE = FREQUENCY+100
NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE

WAVEDATA = ''
for x in range(NUMBEROFFRAMES):
    WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))
for x in range(RESTFRAMES):
    WAVEDATA = WAVEDATA+chr(128)
        
p = PyAudio()
stream = p.open(format = p.get_format_from_width(1),channels = 2,rate = BITRATE,output = True)

while (True):
    try:
        x = 0
        WAVEDATA = ''
        while (is_pressed("d")): 
            x+=1
            WAVEDATA = WAVEDATA+chr(int(math.sin(200/((BITRATE/FREQUENCY)/math.pi))*127+128))
            WAVEDATA = WAVEDATA+chr(128)
            stream.write(WAVEDATA)
            
        #stream.stop_stream()
        #stream.close()
        #p.terminate()
    except KeyboardInterrupt:
        break

