import sys, pygame
from pygame_button import Button

pygame.init()
pygame.font.init()

## this is to set up the font used
leFont = pygame.font.SysFont(None, 30)

## width and height of the screen
size = width, height = 800, 480

screen = pygame.display.set_mode(size)
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY = 130, 130, 130

BUTTON_STYLE = {
    "hover_color":GREY,
    "clicked_color":(70, 70, 70)
}

#######################
# I brought this stuff in from another file in here I used to test the gpio
import RPi.GPIO as GPIO
from time import sleep
from Instruments import *
##import Piano_Chord_Recognition as PCR
from Piano_Chord_Recognition import bigFunk

GPIO.setmode(GPIO.BCM)
# GPIO inputs used
keys = [18, 19, 20, 21, 22, 23, 24, 25, 26, 17, 16, 13]
# used to represent if a key is being pushed down or not
down = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# list of notes in order on the device
my_list = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
##my_list = ['C', 'E', 'G', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
# setup keys as input
GPIO.setup(keys, GPIO.IN, GPIO.PUD_DOWN)

# make a Piano object
piano = Piano()
# starting octive
octive = 2

## This method changes the octive up on screen and gets new audio files
#   for the piano
def changeOctUp():
    global octive
    print("Octave: {}".format(octive))
    if (octive > 2):
        pass
    else:
        octive += 1
        piano.changeOctive(octive)
## This method changes the octive down on screen and gets new audio files
#   for the piano,
#   there had to be 2 functions because of how the button works
def changeOctDown():
    global octive
    print("Octive: {}".format(octive))
    if (octive < 1):
        pass
    else:
        octive += -1
        piano.changeOctive(octive)

# set up octive buttons
up_button = Button((0, 0, 100, 50), (255, 0, 0), changeOctUp, text="up", **BUTTON_STYLE)
up_button.rect.center = (width//4+width//2+width//8, 100)

down_button = Button((0, 0, 100, 50), (255, 0, 0), changeOctDown, text="down", **BUTTON_STYLE)
down_button.rect.center = (width//4+width//2-width//8, 100)

# get background image, I didn't choose the name
bg = pygame.image.load("SEXY_RECTANGLES.gif")

# get the images for the notation
note_img = pygame.image.load("Whole note.png")
sharp_img = pygame.image.load("Whole_note_Sharp.png")
bar = pygame.image.load("Empty_Bar.gif")

## This method puts the corresponding note to the screen for which
#       is being pushed down
def blitNotes():
    x1 = 200
    x2 = 220
    if (down[0]):
        A = note_img
        #screen.blit(A, (200, 150))
        screen.blit(A, (x1, 143))
    if (down[1]):
        As = sharp_img
        screen.blit(As, (x2, 143))
    if (down[2]):
        B = note_img
        screen.blit(B, (x1, 133))
    if (down[3]):
        C = note_img
        screen.blit(C, (x1, 123))
    if (down[4]):
        Cs = sharp_img
        screen.blit(Cs, (x2, 123))
    if (down[5]):
        D = note_img
        screen.blit(D, (x1, 113))
    if (down[6]):
        Ds = sharp_img
        screen.blit(Ds, (x2, 113))
    if (down[7]):
        E = note_img
        screen.blit(E, (x1, 103))
    if (down[8]):
        F = note_img
        screen.blit(F, (x1, 93))
    if (down[9]):
        Fs = sharp_img
        screen.blit(Fs, (x2, 93))
    if (down[10]):
        G = note_img
        screen.blit(G, (x1, 83))
    if (down[11]):
        Gs = sharp_img
        screen.blit(Gs, (x2, 83))

## the mainloop
while (True):
    # checks for events, which in this case are the octive buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        up_button.check_event(event)
        down_button.check_event(event)
    
    # set up the background image
    screen.blit(bg,(0,0))
    place = 0
    #######
    # default text for single note detection
    text_note = "no note"

    # checks to see which gpio keys are down
    # if key is pressed, this uses the lists
    # to play the note, change the down lists so it's not
    # repeated several times, changes text_note to what's being pressed,
    # and if the key is not pressed, changes the down place to 0
    for i in range(len(keys)):
        if (GPIO.input(keys[i]) and down[i] == 0):
            down[i] = 1
            ##print(place)
            place = i
            text_note = my_list[place]
            piano.playNote(i)
        elif (not GPIO.input(keys[i]) and down[i] == 1):
            down[i] = 0
    ##print(down)
    # changes place
    for k in range(len(down)):
        if down[k] == 1:
            place = k

    # these next 4 lines check how many keys are pushed down
    num = 0
    for push in down:
        if (push == 1):
            num += 1
    # only display the single note if only one key is pressed
    if (num == 1):
        text_note = my_list[place]

    # if 3 keys are pressed, check to see if it is a recognizable chord
    if (num == 3 and chord == False):
        temp = []
        relist = []
        for push in range(len(down)):
            if down[push] == 1:
                temp.append(my_list[push])
        text = bigFunk(temp[0], temp[1], temp[2])
        chord = True
        print(temp)
        print(text)
    # set chord text to no chord
    elif (num != 3):
        chord = False
        text = "no chord"
        #print(chord)
    ############3
    # Everthing from here on out just renders everything to the 
    # pygame gui: text, buttons, and images
    temp_text = leFont.render(text, False, BLACK)
    screen.blit(temp_text, (width//5, height/2+height/4-height//9))
    chord_title = leFont.render("Chord Recognition", False, WHITE)
    screen.blit(chord_title, (width//5-50, height/2+height/4-height//5))

    temp_note = leFont.render(text_note, False, BLACK)
    screen.blit(temp_note, (width//2 + width//4 - 20, height/2+height/4-height//9))
    note_title = leFont.render("Note Recognition", False, WHITE)
    screen.blit(note_title, (width//2 + width//4 - 70, height/2+height/4-height//5))
    up_button.update(screen)
    down_button.update(screen)
    octive_text = leFont.render(str(octive), False, BLACK)
    screen.blit(octive_text, (width//2+width//4, 150))
    
    octive_title = leFont.render("Octive", False, WHITE)
    screen.blit(octive_title, (width//2+width//4-30, 30))

    notation_title = leFont.render("Notation", False, WHITE)
    screen.blit(notation_title, (width//2 - width//4 - 50, 30))
    screen.blit(bar, (100, 70))
    blitNotes()
        
    pygame.display.flip()
