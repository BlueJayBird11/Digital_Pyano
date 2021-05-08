import sys, pygame
from pygame_button import Button

pygame.init()
pygame.font.init()

leFont = pygame.font.SysFont(None, 30)


size = width, height = 800, 480

screen = pygame.display.set_mode(size)
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY = 130, 130, 130
screen.fill(WHITE)

BUTTON_STYLE = {
    "hover_color":GREY,
    "clicked_color":(70, 70, 70)
}

#######################3
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
octive = 2

def changeOctUp():
    global octive
    print("Octive: {}".format(octive))
    if (octive > 2):
        pass
    else:
        octive += 1
        piano.changeOctive(octive)

def changeOctDown():
    global octive
    print("Octive: {}".format(octive))
    if (octive < 1):
        pass
    else:
        octive += -1
        piano.changeOctive(octive)


up_button = Button((0, 0, 100, 50), (255, 0, 0), changeOctUp, text="up", **BUTTON_STYLE)
up_button.rect.center = (width//4+width//2+width//8, 100)

down_button = Button((0, 0, 100, 50), (255, 0, 0), changeOctDown, text="down", **BUTTON_STYLE)
down_button.rect.center = (width//4+width//2-width//8, 100)

bg = pygame.image.load("SEXY_RECTANGLES.gif")

note_img = pygame.image.load("Whole note.png")
sharp_img = pygame.image.load("Whole_note_Sharp.png")
bar = pygame.image.load("Empty_Bar.gif")

def blitNotes():
    if (down[0]):
        A = note_img
        #screen.blit(A, (200, 150))
        screen.blit(A, (200, 143))
    if (down[1]):
        As = sharp_img
        screen.blit(As, (220, 143))
    if (down[2]):
        B = note_img
        screen.blit(B, (200, 133))
    if (down[3]):
        C = note_img
        screen.blit(C, (200, 123))
    if (down[4]):
        Cs = sharp_img
        screen.blit(Cs, (220, 123))
    if (down[5]):
        D = note_img
        screen.blit(D, (200, 113))
    if (down[6]):
        Ds = sharp_img
        screen.blit(Ds, (220, 113))
    if (down[7]):
        E = note_img
        screen.blit(E, (200, 103))
    if (down[8]):
        F = note_img
        screen.blit(F, (200, 93))
    if (down[9]):
        Fs = sharp_img
        screen.blit(Fs, (220, 93))
    if (down[10]):
        G = note_img
        screen.blit(G, (200, 83))
    if (down[11]):
        Gs = sharp_img
        screen.blit(Gs, (220, 83))

##def event_loop():
##    pass

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        up_button.check_event(event)
        down_button.check_event(event)
    
    ##screen.fill(background)
    screen.blit(bg,(0,0))
    place = 0
    #######
    text_note = "no note"
    
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
    for k in range(len(down)):
        if down[k] == 1:
            place = k
    num = 0
    for push in down:
        if (push == 1):
            num += 1
    
    if (num == 1):
        text_note = my_list[place]
    
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
    elif (num != 3):
        chord = False
        text = "no chord"
        #print(chord)
    ############3
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
