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


_start_position = (100, 220)
_quit_position = (200, 220)
_pause_position = (64, 220)
_fast_position = (128, 220)
_slow_position = (192, 220)
_back_position = (256, 220)
coordinates_position = (160, 50)


# pygame balls initialization
b1 = pygame.image.load("./cornell.png")
rect1 = b1.get_rect()
rect1.__setattr__("left", 0)
speed1 = [4, 2]
b2 = pygame.image.load("./berkeley.png")
rect2 = b2.get_rect()
rect2.__setattr__("right", 320)
speed2 = [1, 7]

# parameters used to control
_stick_count = 0
_moving = -1
_command_page = 1
_quit = False


# texts initialization
command_level1 = pygame.font.Font(None, 25)
command_level2 = pygame.font.Font(None, 22)
coordinates_field = pygame.font.Font(None, 20)
coordiantes_text = ""

# command buttons definition
# level1
quit_surface = command_level1.render('Quit', True, WHITE)
quit_rect = quit_surface.get_rect(center=_quit_position)
start_surface = command_level1.render("Start", True, WHITE)
start_rect = start_surface.get_rect(center=_start_position)
#level2
pause_surface = command_level2.render("Pause", True, WHITE)
pause_rect = pause_surface.get_rect(center=_pause_position)
fast_surface = command_level2.render("Fast", True, WHITE)
fast_rect = fast_surface.get_rect(center=_fast_position)
slow_surface = command_level2.render("Slow", True, WHITE)
slow_rect = slow_surface.get_rect(center=_slow_position)
back_surface = command_level2.render("Back", True, WHITE)
back_rect = back_surface.get_rect(center=_back_position)


def initiation():
    """
    initiate the pygame display, showing the two buttons
    :return:
    """
    screen.fill(BLACK)
    showBalls()
    showControlButton()
    pygame.display.flip()
    _quit = False


def showControlButton():
    """
    show the control buttons on the pygame
    :return: None
    """
    if _command_page == 1:
        screen.blit(quit_surface, quit_rect)
        screen.blit(start_surface, start_rect)
    elif _command_page == 2:
        screen.blit(pause_surface, pause_rect)
        screen.blit(fast_surface, fast_rect)
        screen.blit(slow_surface, slow_rect)
        screen.blit(back_surface, back_rect)


def showCoordinates():
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

    while not _quit:
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

                if _command_page == 1:
                    if quit_rect.left < x < quit_rect.right and quit_rect.top < y < quit_rect.bottom:
                        print("Quit button pressed!")
                        _quit = True
                        break
                    elif start_rect.left < x < start_rect.right and start_rect.top < y < start_rect.bottom:
                        print("Start button pressed!")
                        _command_page = 2
                        _moving = 1
                    else:
                        coordiantes_text = "(" + str(x) + "," + str(y) + ") is pressed."
                        print(coordiantes_text)
                elif _command_page == 2:
                    if pause_rect.left < x < pause_rect.right and pause_rect.top < y < pause_rect.bottom:
                        print("Pause button pressed!")
                        _moving = _moving * -1
                    elif fast_rect.left < x < fast_rect.right and fast_rect.top < y < fast_rect.bottom:
                        print("Fast button pressed!")
                        if speed1[0] >= 0:
                            speed1[0] += 1
                        else:
                            speed1[0] -= 1
                        if speed1[1] >= 0:
                            speed1[1] += 1
                        else:
                            speed1[1] -= 1
                        if speed2[0] >= 0:
                            speed2[0] += 1
                        else:
                            speed2[0] -= 1
                        if speed2[1] >= 0:
                            speed2[1] += 1
                        else:
                            speed2[1] -= 1
                    elif slow_rect.left < x < slow_rect.right and slow_rect.top < y < slow_rect.bottom:
                        print("Slow button pressed!")
                        if speed1[0] > 0:
                            speed1[0] -= 1
                        else:
                            speed1[0] += 1
                        if speed1[1] > 0:
                            speed1[1] -= 1
                        else:
                            speed1[1] += 1
                        if speed2[0] > 0:
                            speed2[0] -= 1
                        else:
                            speed2[0] += 1
                        if speed2[1] > 0:
                            speed2[1] -= 1
                        else:
                            speed2[1] += 1
                    elif back_rect.left < x < back_rect.right and back_rect.top < y < back_rect.bottom:
                        print("Back button pressed!")
                        _moving = -1
                        _command_page = 1
                    else:
                        coordiantes_text = "(" + str(x) + "," + str(y) + ") is pressed."
                        print(coordiantes_text)

        showCoordinates()
        if _moving > 0:
            rect1 = rect1.move(speed1)
            rect2 = rect2.move(speed2)
            speed1, speed2, _stick_count = ballsMovement(speed1, speed2, _stick_count)
        showBalls()
        showControlButton()
        pygame.display.flip()

