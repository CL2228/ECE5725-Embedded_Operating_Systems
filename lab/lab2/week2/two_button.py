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
start_position = (100, 220)
quit_position = (200, 220)
clear_position = (270, 220)
coordinates_position = (160, 50)
quit_mode = False

# pygame balls initialization
b1 = pygame.image.load("./cornell.png")
rect1 = b1.get_rect()
rect1.__setattr__("left", 0)
speed1 = [4, 2]
b2 = pygame.image.load("./berkeley.png")
rect2 = b2.get_rect()
rect2.__setattr__("right", 320)
speed2 = [1, 7]
_stick_count = 0
_moving = -1

# texts initialization
control_button = pygame.font.Font(None, 25)
coordinates_field = pygame.font.Font(None, 20)
coordiantes_text = ""

quit_surface = control_button.render('Quit', True, WHITE)
quit_rect = quit_surface.get_rect(center=quit_position)
start_surface = control_button.render("Start/Pause", True, WHITE)
start_rect = start_surface.get_rect(center=start_position)
clear_surface = control_button.render("Clear", True, WHITE)
clear_rect = clear_surface.get_rect(center = clear_position)


def initiation():
    """
    initiate the pygame display, showing the two buttons
    :return:
    """
    screen.fill(BLACK)
    showBalls()
    showControlButton()
    pygame.display.flip()
    quit_mode = False


def showControlButton():
    """
    show the control buttons on the pygame
    :return: None
    """
    screen.blit(quit_surface, quit_rect)
    screen.blit(start_surface, start_rect)
    screen.blit(clear_surface, clear_rect)


def showCoordinates():
    # text = "(" + str(x) + "," + str(y) + ") is pressed."
    coordinate_surface = coordinates_field.render(coordiantes_text, True, WHITE)
    coordinate_rect = coordinate_surface.get_rect(center=coordinates_position)
    screen.blit(coordinate_surface, coordinate_rect)


def showBalls():
    screen.blit(b1, rect1)
    screen.blit(b2, rect2)


def ballsMovement(speed1, speed2, stick_count):
    if (math.sqrt(math.pow(rect1.centerx - rect2.centerx, 2) + math.pow(rect1.centery - rect2.centery, 2)) < 50):
        r1, r2 = np.array(rect1.center), np.array(rect2.center)
        d = np.linalg.norm(r1 - r2) ** 2
        v1, v2 = np.array(speed1), np.array(speed2)
        u1 = v1 - np.dot(v1 - v2, r1 - r2) / d * (r1 - r2)
        u2 = v2 - np.dot(v2 - v1, r2 - r1) / d * (r2 - r1)
        speed1 = [u1[0], u1[1]]
        speed2 = [u2[0], u2[1]]
        stick_count += 1
        if stick_count > 50:
            rect1.__setattr__("right", 320)
            rect1.__setattr__("top", 0)
            rect2.__setattr__("left", 0)
            rect2.__setattr__("top", 0)
    else:
        stick_count = 0

    if rect1.left < 0:
        speed1[0] = abs(speed1[0])
    if rect1.right > width:
        speed1[0] = -abs(speed1[0])
    if rect1.top < 0:
        speed1[1] = abs(speed1[1])
    if rect1.bottom > height:
        speed1[1] = -abs(speed1[1])

    if rect2.left < 0:
        speed2[0] = abs(speed2[0])
    if rect2.right > width:
        speed2[0] = -abs(speed2[0])

    if rect2.top < 0:
        speed2[1] = abs(speed2[1])
    if rect2.bottom > height:
        speed2[1] = -abs(speed2[1])

    return speed1, speed2, stick_count

if __name__ == "__main__":
    initiation()
    print("hello, pygame is running...")

    while not quit_mode:
        time.sleep(0.02)
        # if (not GPIO.input(27)):
        #     # print (" ")
        #     # print "Button 27 pressed...."
        #     break;

        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x, y = pos

                if quit_rect.left < x < quit_rect.right and quit_rect.top < y < quit_rect.bottom:
                    print("quit button pressed!")
                    quit_mode = True
                    break
                elif start_rect.left < x < start_rect.right and start_rect.top < y < start_rect.bottom:
                    print("start/pause button pressed!")
                    _moving = _moving * -1
                elif clear_rect.left < x < clear_rect.right and clear_rect.top < y < clear_rect.bottom:
                    print("clear button pressed!")
                    coordiantes_text = ""
                else:
                    coordiantes_text = "(" + str(x) + "," + str(y) + ") is pressed."
                    print(coordiantes_text)

                    # showControlButton()
                    # showCoordinates(pos)

        showCoordinates()
        if _moving > 0:
            rect1 = rect1.move(speed1)
            rect2 = rect2.move(speed2)
            speed1, speed2, _stick_count = ballsMovement(speed1, speed2, _stick_count)
        showBalls()
        showControlButton()
        pygame.display.flip()

