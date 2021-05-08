import sys, pygame

pygame.init()
pygame.font.init()

leFont = pygame.font.SysFont(None, 30)


size = width, height = 800, 480

screen = pygame.display.set_mode(size)
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY = 130, 130, 130
screen.fill(WHITE)
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



bg = pygame.image.load("SEXY_RECTANGLES.gif")

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
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
    
    pygame.display.flip()
