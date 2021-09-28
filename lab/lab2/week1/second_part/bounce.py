import pygame
import os
import time
import RPi.GPIO as GPIO
import subprocess

# os.putenv('SDL_VIDEODRIVER', 'fbcon')
# os.putenv('SDL_FBDEV', '/dev/fb1')

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)



if __name__ == "__main__":



    size = width, height = 320, 240
    speed = [1, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    ball = pygame.image.load("test.png")
    ballRect = ball.get_rect()

    while True:
        if (not GPIO.input(27)):
            # print (" ")
            # print "Button 27 pressed...."
            break;


        time.sleep(0.02)
        ballRect = ballRect.move(speed)
        if ballRect.left < 0 or ballRect.right > width:
            speed[0] = -speed[0]
        if ballRect.top < 0 or ballRect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballRect)
        pygame.display.flip()


