import math
import pyaudio
import pygame

pygame.init()
class Instrument:
    def __init__(self):
        pass

    def testSound(self):
        sound = pygame.mixer.Sound("Notes/Piano/A.wav")
        sound.play()

    def playSound(self, location):
        sound = pygame.mixer.Sound(location)
        sound.play()

class Piano(Instrument):
    def __init__(self):
        super().__init__()

    def playNote(self, value):
        if (value==0):
            self.playSound("Notes/Piano/D.wav")
        if (value==1):
            self.playSound("Notes/Piano/D_s.wav")
        if (value==2):
            self.playSound("Notes/Piano/E.wav")
        if (value==3):
            self.playSound("Notes/Piano/F.wav")
        if (value==4):
            self.playSound("Notes/Piano/F_s.wav")
        if (value==5):
            self.playSound("Notes/Piano/G.wav")
        if (value==6):
            self.playSound("Notes/Piano/G_s.wav")
        if (value==7):
            self.playSound("Notes/Piano/A.wav")
        if (value==8):
            self.playSound("Notes/Piano/Bb.wav")
        if (value==9):
            self.playSound("Notes/Piano/B.wav")
        if (value==10):
            self.playSound("Notes/Piano/C.wav")
        if (value==11):
            self.playSound("Notes/Piano/C_s.wav")


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