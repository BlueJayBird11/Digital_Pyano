import math
import rip
import pygame

pygame.init()
class Instrument:
    def __init__(self, name="none"):
        self.name = name
        self.octive = 2
        self.keys = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    @property
    def octive(self):
        return self._octive
    
    @octive.setter
    def octive(self, value):
        if (-1 < value < 7):
            self._octive = value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    def testSound(self):
        sound = pygame.mixer.Sound("Notes/Piano/0.wav")
        sound.play()

    def playSound(self, location):
        sound = pygame.mixer.Sound(location)
        sound.play()

    def press_down(self, place):
        self.keys[place] = 1

    def press_up(self, place):
        self.keys[place] = 0

class Piano(Instrument):
    def __init__(self):
        super().__init__("Piano")
        rip.getNotes(2)

    def changeOctive(self, value):
        self.octive = value
        rip.getNotes(self.octive)

    def playNote(self, value):
##        print("clicked {}".format(value))
        if (value==0):
            self.playSound("Notes/Piano/0.wav")
        if (value==1):
            self.playSound("Notes/Piano/1.wav")
        if (value==2):
            self.playSound("Notes/Piano/2.wav")
        if (value==3):
            self.playSound("Notes/Piano/3.wav")
        if (value==4):
            self.playSound("Notes/Piano/4.wav")
        if (value==5):
            self.playSound("Notes/Piano/5.wav")
        if (value==6):
            self.playSound("Notes/Piano/6.wav")
        if (value==7):
            self.playSound("Notes/Piano/7.wav")
        if (value==8):
            self.playSound("Notes/Piano/8.wav")
        if (value==9):
            self.playSound("Notes/Piano/9.wav")
        if (value==10):
            self.playSound("Notes/Piano/10.wav")
        if (value==11):
            self.playSound("Notes/Piano/11.wav")


class Wave(Instrument):
    def __init__(self):
        super().__init__("Wave")
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
