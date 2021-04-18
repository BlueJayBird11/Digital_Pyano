import math
import pyaudio

class Instrument:
    def __init__(self):
        pass

class Piano(Instrument):
    def __init__(self):
        super().__init__()
        self.wav = []

class Wave(Instrument):
    def __init__(self):
        super().__init__()
        self.f0 = 440.00


    def getHalfSteps(self, other):
        h_steps = other
        return h_steps

    def getF(self, note):
        n = self.getHalfSteps(note)
        return self.f0 * (2**(1/12))**n

    def changeOctive(self, direction):
        pass

    def playSound(self, note):
        pass