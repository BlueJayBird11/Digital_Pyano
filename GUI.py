from tkinter import *

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
###############VVVSheet Music LinesVVV#################
        self.create_rectangle(0, 310, 200, 305, fill='black')
        self.create_rectangle(0, 325, 200, 325)
        self.create_rectangle(0, 340, 200, 340)
        self.create_rectangle(0, 355, 200, 355)
        self.create_rectangle(0, 370, 200, 370)
        self.create_rectangle(0, 385, 200, 385)
        self.create_rectangle(0, 400, 200, 405, fill='black')
######################################################
###############VVVShapes that will be buttonsVVV#################
        points1= [450, 100,  475, 120, 425, 100, 475, 80]
        points2= [625, 100,  600, 120, 650, 100, 600, 80]
        ##points3= [50, 250,  70, 275, 50, 225, 30, 275]
        ##points4= [50, 325,  70, 300, 50, 350, 30, 300] 
#[Front(125, 150),  Bottom(175, 170), Center(150, 150), Top(175, 130)]###
        triangleButton1 = self.create_polygon(points1, outline='black')
        triangleButton2 = self.create_polygon(points2, outline='black')
        ##triangleButton3 = self.create_polygon(points3, outline='black')
        ##triangleButton4 = self.create_polygon(points4, outline='black')
#############################################################
        #################VVVLabelsVVV#################
        ####Note Name####
        noteE = Label(mainWindow, text='E', bg="#FDA7DF", fg='black')
        noteE.place(relx=1.0, rely=1.0, x=-570, y=-155, anchor='se')
##        noteD = Label(mainWindow, text='D', bg="#FDA7DF", fg='black')
##        noteD.place(relx=1.0, rely=1.0, x=-570, y=-145, anchor='se')
        ##noteDD = Label(mainWindow, text='D#', bg="#FDA7DF", fg='white')
        ##noteDD.place(relx=1.0, rely=1.0, x=-570, y=-155, anchor='se')
        noteC = Label(mainWindow, text='C', bg="#FDA7DF", fg='black')
        noteC.place(relx=1.0, rely=1.0, x=-570, y=-135, anchor='se')
        ##noteCC = Label(mainWindow, text='C#', bg="#FDA7DF", fg='white')
        ##noteCC.place(relx=1.0, rely=1.0, x=-570, y=-135, anchor='se')
        noteB = Label(mainWindow, text='B', bg="#FDA7DF", fg='black')
        noteB.place(relx=1.0, rely=1.0, x=-570, y=-115, anchor='se')
        noteA = Label(mainWindow, text='A', bg="#FDA7DF", fg='black')
        noteA.place(relx=1.0, rely=1.0, x=-570, y=-95, anchor='se')
        ##noteAA = Label(mainWindow, text='A#', bg="#FDA7DF", fg='white')
        ##noteAA.place(relx=1.0, rely=1.0, x=-570, y=-95, anchor='se')
        noteG = Label(mainWindow, text='G', bg="#FDA7DF", fg='black')
        noteG.place(relx=1.0, rely=1.0, x=-570, y=-75, anchor='se')
        ##noteGG = Label(mainWindow, text='G#', bg=""#FDA7DF"-75, anchor='se')
        ##noteG.place(relx=1.0, rely=1.0, x=-570, y=-75, anchor='se')
        noteF = Label(mainWindow, text='F', bg="#FDA7DF", fg='black')
        noteF.place(relx=1.0, rely=1.0, x=-570, y=-55, anchor='se')
        ##noteDD = Label(mainWindow, text='F#', bg="#FDA7DF", fg='white')
        ##noteDD.place(relx=1.0, rely=1.0, x=-570, y=-175, anchor='se')
        ######Instrument Name####
        ##instrumentName = Label(mainWindow, text='Replace with name', bg='white', fg='black')
        ##instrumentName.pack()
        ############################################
        T = Text(mainWindow, height = int(CONSTANT/2), width = int(WIDTH/4))
        l = Label(mainWindow, text = "Choard")
        l.config(font =("Courier", 14))
        

CONSTANT = 60
WIDTH = 800
HEIGHT = 480
mainWindow.geometry("{}x{}".format(WIDTH, HEIGHT))
s = windows(mainWindow)
s.lower(mainWindow)
s.grids()

mainWindow.mainloop()
