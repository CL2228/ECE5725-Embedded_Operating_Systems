import os
import math
import time
import pygame
import numpy as np
from pygame.locals import *     # input events

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


if __name__ == "__main__":

    print("hello, pygame is running...")


    # pygame balls initialization
    b1 = pygame.image.load("./cornell.png")
    rect1 = b1.get_rect()
    rect1.__setattr__("right", 320)

    # texts initialization
    my_font = pygame.font.Font(None, 50)
    my_buttons = {'button1': (80, 180), 'button2': (240, 180)}
    screen.fill(BLACK)
    for my_text, text_pos in my_buttons.items():
        text_surface = my_font.render(my_text, True, WHITE)
        text_rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, text_rect)
        print(text_rect)


    pygame.display.flip()



    while True:

        for event in pygame.event.get():
            # print(event)
            if event.type == MOUSEBUTTONDOWN:
                # print("mouse down")
                pos = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONUP:
                # print("mouse up")
                pos = pygame.mouse.get_pos()
                x, y = pos
                if y > 120:
                    if x < 160:
                        print("button1 pressed")
                    else:
                        print("button2 pressed")

