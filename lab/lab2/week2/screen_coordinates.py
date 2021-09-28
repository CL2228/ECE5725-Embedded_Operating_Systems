import os
import math
import time
import pygame
import numpy as np
from pygame.locals import *     # input events
# import RPi.GPIO as GPIO

# GPIO button for quit
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# un-comment these statements when using monitor!
# os.putenv('SDL_VIDEODRIVER', 'fbcon')       # display on piTFT
# os.putenv('SDL_FBDEV', '/dev/fb1')
# os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

# pygame screen initialization
pygame.init()
size = (width, height) = (320, 240)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.mouse.set_visible(True)      # True for monitor, False for piTFT
screen = pygame.display.set_mode(size)

quit_position = (160, 220)
coordinates_position = (160, 50)

if __name__ == "__main__":

    print("hello, pygame is running...")


    # pygame balls initialization
    b1 = pygame.image.load("./cornell.png")
    rect1 = b1.get_rect()
    rect1.__setattr__("right", 320)

    # texts initialization
    my_font = pygame.font.Font(None, 25)
    screen.fill(BLACK)
    quit_surface = my_font.render('quit', True, WHITE)
    quit_rect = quit_surface.get_rect(center=quit_position)
    screen.blit(quit_surface, quit_rect)

    pygame.display.flip()

    quit = False

    while not quit:
        # time.sleep(0.02)
        # if (not GPIO.input(27)):
        #     # print (" ")
        #     # print "Button 27 pressed...."
        #     break;

        for event in pygame.event.get():
            # print(event)
            if event.type == MOUSEBUTTONDOWN:
                # print("mouse down")
                pos = pygame.mouse.get_pos()
                x, y = pos


            elif event.type == MOUSEBUTTONUP:
                # print("mouse up")
                pos = pygame.mouse.get_pos()
                x, y = pos

                if x > quit_rect.left and x < quit_rect.right and y > quit_rect.top and y < quit_rect.bottom:
                    print("quit button pressed!")
                    quit = True
                    break
                else:
                    text = "(" + str(x) + "," + str(y) + ") is pressed."
                    screen.fill(BLACK)

                    quit_surface = my_font.render('quit', True, WHITE)
                    quit_rect = quit_surface.get_rect(center=quit_position)
                    screen.blit(quit_surface, quit_rect)

                    coordinate_surface = my_font.render(text, True, WHITE)
                    coordinate_rect = coordinate_surface.get_rect(center=coordinates_position)
                    screen.blit(coordinate_surface, coordinate_rect)

                    pygame.display.flip()
                    print(text)























