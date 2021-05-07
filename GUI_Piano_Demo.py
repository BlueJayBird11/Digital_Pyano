from tkinter import *
from PIL import ImageTk,Image
from time import sleep

mainWindow = Tk()
mainWindow.title("Digital Piano")


class windows(Canvas):
    def __init__(self, mainWindow):
        Canvas.__init__(self, mainWindow, width = WIDTH, height = HEIGHT)
        self.place(relx=1.0, rely=1.0, x=0, y=0, anchor='se')
        

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
#########New stuff#########
        Label_1 = Label(mainWindow, bg = "#6F1E51", text = "Temp label for chord reader", fg='white', font = ("Arial", 20))
        Label_1.place(relx = 0.035, rely = 0.300)

        Label_2 = Label(mainWindow, bg = "#006266", text = "Temp Label for Note", fg='white', font = ("Arial", 20))
        Label_2.place(relx = 0.600, rely = 0.720)
#########
        B1 = Button(mainWindow, bg = "white", text = "  SHIFT UP   ",  font = ("Arial", 22))
        B1.place(relx = 0.498, rely = 0.20)
        

        B2 = Button(mainWindow, bg = "white", text = "SHIFT DOWN", font = ("Arial", 22))
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
        def noteDisplay():
            load = Image.open('Whole_note.gif')
            render = ImageTk.PhotoImage(load)
            
            img1 = Label(self, image=render)
            img1.image = render
            img1.place(x=325, y=347)

            img2 = Label(self, image=render)
            img2.image = render
            img2.place(x=275, y=355)

            img3 = Label(self, image=render)
            img3.image = render
            img3.place(x=225, y=362)

            img4 = Label(self, image=render)
            img4.image = render
            img4.place(x=175, y=370)

            img5 = Label(self, image=render)
            img5.image = render
            img5.place(x=325, y=378)

            img6 = Label(self, image=render)
            img6.image = render
            img6.place(x=275, y=385)

            img7 = Label(self, image=render)
            img7.image = render
            img7.place(x=225, y=393)

            img8 = Label(self, image=render)
            img8.image = render
            img8.place(x=175, y=400)

            img9 = Label(self, image=render)
            img9.image = render
            img9.place(x=325, y=407)

        ############################################
        T = Text(mainWindow, height = CONSTANT/2, width = int(WIDTH/4))
        l = Label(mainWindow, text = "Choard")
        l.config(font =("Courier", 14))
        mainWindow.title("Digital Pyano")
        

CONSTANT = 60
WIDTH = 800
HEIGHT = 480
mainWindow.geometry("{}x{}".format(WIDTH, HEIGHT))
s = windows(mainWindow)
s.lower(mainWindow)
s.grids()

mainWindow.mainloop()
