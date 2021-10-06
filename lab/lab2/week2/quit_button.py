"""
Author: Chenghui Li (cl2228)

This file is also uploaded to Github: https://github.com/CL2228/ECE5725-Embedded_Operating_Systems

Group members: Chenghui Li (cl2228); Hehong Li(hl778)
Lab2, Week2

!!NOTICE: Since my program works well, and I can quit the program with the GPIO button,
            I didn't add a timer to quit the program because it is unnecessary.

this python program is for quiting the program is the quit button is pressed
1. Quit: when pressing the quit button, the whole program quits

"""
import os
import math
import time
import pygame
import numpy as np
from pygame.locals import *     # input events
import RPi.GPIO as GPIO

# GPIO button for quit
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# un-comment these statements when using monitor!
os.putenv('SDL_VIDEODRIVER', 'fbcon')       # display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')



# pygame screen initialization
pygame.init()                               # initialize the pygame
size = (width, height) = (320, 240)         # set up the size
BLACK = (0, 0, 0)                           # backgrounds
WHITE = (255, 255, 255)
pygame.mouse.set_visible(False)             # True for monitor, False for piTFT
screen = pygame.display.set_mode(size)


if __name__ == "__main__":

    print("hello, pygame is running...")


    # pygame balls initialization
    b1 = pygame.image.load("./cornell.png")
    rect1 = b1.get_rect()
    rect1.__setattr__("right", 320)

    # texts initialization
    my_font = pygame.font.Font(None, 25)
    my_font.set_bold(True)
    my_buttons = {'button1': (80, 180), 'button2': (240, 180)}
    screen.fill(BLACK)

    text_surface = my_font.render('quit', True, WHITE)
    text_rect = text_surface.get_rect(center=(160, 200))
    screen.blit(text_surface, text_rect)
    quit = False

    pygame.display.flip()

    while not quit:
        time.sleep(0.02)
        if (not GPIO.input(27)):                        # the GPIO button is pressed
            # print (" ")
            # print "Button 27 pressed...."
            break

        for event in pygame.event.get():
            # print(event)
            if event.type == MOUSEBUTTONDOWN:
                # print("mouse down")
                pos = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONUP:
                # print("mouse up")
                pos = pygame.mouse.get_pos()            # quit the program is quit button is pressed
                x, y = pos
                if x > text_rect.left and x < text_rect.right and y > text_rect.top and y < text_rect.bottom:
                    print("quit!")
                    quit = True
                    break

