from tkinter import *
from PIL import ImageTk,Image
from Instruments import *
import pigpio


mainWindow = Tk()
mainWindow.title("Digital Piano")


class windows(Canvas):
    def __init__(self, mainWindow):
        Canvas.__init__(self, mainWindow, width = WIDTH, height = HEIGHT)
        self.place(relx=1.0, rely=1.0, x=0, y=0, anchor='se')
        self.octive = 2
        self.keys = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.instrument = Piano()

        #
##        self.pi = pigpio.pi()
##        octkeys = [18, 19, 20, 21, 22]
##        # self.pi.set_mode(18, pigpio.INPUT)
##        for key in octkeys:
##            self.pi.set_mode(key, pigpio.INPUT)
##            #self.pi.callback(key, pigpio.EITHER_EDGE, self.playNote)
##            self.pi.callback(key, pigpio._EDGE, self.playNote)

    def playNote(self, gpio, level, tick):
        # print(level)
        print("gpio:{}, level:{}, ticks:{}".format(gpio, level, tick))
        if (gpio == 18 and level == 1 and self.keys[0] == 0):
            self.instrument.playNote(0)
            print("hit")
            self.keys[0] = 1
        elif():
            self.keys[0] = 0
        if (gpio == 19 and level == 1 and self.keys[0] == 0):
            self.instrument.playNote(0)
            print("hit")
            self.keys[1] = 1
        elif():
            self.keys[1] = 0

    def grids(self):
        self.create_rectangle(WIDTH/2, HEIGHT/2, 0, 0, fill = "#6F1E51")
        self.create_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, fill = "#006266")
        self.create_rectangle(WIDTH/2, HEIGHT/2, WIDTH, 0, fill = "#9980FA")
        self.create_rectangle(WIDTH/2, HEIGHT/2, 0, HEIGHT, fill = "#FDA7DF")
        
        self.create_rectangle(0, 0, WIDTH/2, CONSTANT, fill = "white")
        self.create_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT/2 + CONSTANT, fill = "white")
        self.create_rectangle(WIDTH/2, HEIGHT/2, 0, HEIGHT/2 + CONSTANT, fill = "white")
        self.create_rectangle(WIDTH/2, 0, WIDTH, CONSTANT, fill = "white")
        Label_1 = Label(mainWindow, bg = "white", text = "Chord Reader", font = ("Arial", 26))
        Label_1.place(relx = 0.125, rely = 0.02)

        Label_2 = Label(mainWindow, bg = "white", text = "Octave Shift", font = ("Arial", 26))
        Label_2.place(relx = 0.640, rely = 0.02)

        Label_2 = Label(mainWindow, bg = "white", text = "Sheet Music", font = ("Arial", 26))
        Label_2.place(relx = 0.125, rely = 0.520)

        Label_2 = Label(mainWindow, bg = "white", text = "Note", font = ("Arial", 26))
        Label_2.place(relx = 0.700, rely = 0.520)
        
        B1 = Button(mainWindow, bg = "white", text = "  SHIFT UP   ", font = ("Arial", 22), command=self.changeOct(1))
        B1.place(relx = 0.498, rely = 0.20)

        B2 = Button(mainWindow, bg = "white", text = "SHIFT DOWN", font = ("Arial", 22), command=self.changeOct(-1))
        B2.place(relx = 0.730, rely = 0.20)
        
        
###############VVVSheet Music LinesVVV#################
        self.create_rectangle(50, 340, 350, 345, fill='black')
        self.create_rectangle(50, 355, 350, 355)
        self.create_rectangle(50, 370, 350, 370)
        self.create_rectangle(50, 385, 350, 385)
        self.create_rectangle(50, 400, 350, 400)
        self.create_rectangle(50, 415, 350, 415)
        self.create_rectangle(50, 430, 350, 425, fill='black')
######################################################
        ####Whole note function####
        load = Image.open('Whole_note.gif')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=300, y=355)
        ############################################
        T = Text(mainWindow, height = CONSTANT/2, width = int(WIDTH/4))
        l = Label(mainWindow, text = "Choard")
        l.config(font =("Courier", 14))
        mainWindow.title("Digital Pyano")

    def changeOct(self, value):
        self.octive += value
        # get new wav files from instrument
        self.instrument.changeOctive(value)
        print(self.octive)

CONSTANT = 60
WIDTH = 800
HEIGHT = 480
mainWindow.geometry("{}x{}".format(WIDTH, HEIGHT))
s = windows(mainWindow)
s.lower(mainWindow)
s.grids()

pi = pigpio.pi()
octkeys = [18, 19, 20, 21, 22]
# self.pi.set_mode(18, pigpio.INPUT)
#for key in octkeys:
#    pi.set_mode(key, pigpio.INPUT)
#    #self.pi.callback(key, pigpio.EITHER_EDGE, self.playNote)
#    pi.callback(key, pigpio.FALLING_EDGE, s.playNote)
pi.callback(18, pigpio.EITHER_EDGE, s.playNote)
pi.callback(19, pigpio.EITHER_EDGE, s.playNote)


mainWindow.mainloop()
#GPIO.cleanup()
