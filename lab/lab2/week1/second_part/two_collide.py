import math
import time
import pygame
import numpy as np
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')

if __name__ == "__main__":
    size = width, height = 320, 240
    speed1 = [4, 2]
    speed2 = [1, 7]
    black = 0, 0, 0

    r = 25

    screen = pygame.display.set_mode(size)
    ball1 = pygame.image.load("berkeley.png")
    ball1Rect = ball1.get_rect()
    ball2 = pygame.image.load("cornell.png")
    ball2Rect = ball2.get_rect()

    ball1Rect.__setattr__("right", 320)
    print(ball1Rect.center[0])

    cnt = 0
    while True:
        time.sleep(0.02)

        time.sleep(0.02)
        if (not GPIO.input(27)):
            # print (" ")
            # print "Button 27 pressed...."
            break;

        ball1Rect = ball1Rect.move(speed1)
        ball2Rect = ball2Rect.move(speed2)


        if (math.sqrt(math.pow(ball1Rect.centerx- ball2Rect.centerx, 2) + math.pow(ball1Rect.centery- ball2Rect.centery, 2)) < 50) :
            r1, r2 = np.array(ball1Rect.center), np.array(ball2Rect.center)
            d = np.linalg.norm(r1 - r2) ** 2
            v1, v2 = np.array(speed1), np.array(speed2)
            u1 = v1 - np.dot(v1-v2, r1 - r2) / d * (r1 - r2)
            u2 = v2 - np.dot(v2-v1, r2 - r1) / d * (r2 - r1)
            speed1 = [u1[0], u1[1]]
            speed2 = [u2[0], u2[1]]
            cnt += 1
            if cnt > 50:
                ball1Rect.__setattr__("right", 320)
                ball1Rect.__setattr__("top", 0)
                ball2Rect.__setattr__("left", 0)
                ball2Rect.__setattr__("top", 0)

        else:
            cnt = 0
            # speed1[0] = -speed1[0]
            # speed2[0] = -speed2[0]
            # speed1[1] = -speed1[1]
            # speed2[1] = -speed2[1]

        if ball1Rect.left < 0:
            speed1[0] = abs(speed1[0])
        if ball1Rect.right > width:
            speed1[0] = -abs(speed1[0])

        if ball1Rect.top < 0 :
            speed1[1] = abs(speed1[1])
        if ball1Rect.bottom > height:
            speed1[1] = -abs(speed1[1])


        if ball2Rect.left < 0 :
            speed2[0] = abs(speed2[0])
        if ball2Rect.right > width :
            speed2[0] = -abs(speed2[0])

        if ball2Rect.top < 0 :
            speed2[1] = abs(speed2[1])
        if ball2Rect.bottom > height:
            speed2[1] = -abs(speed2[1])

        screen.fill(black)
        screen.blit(ball1, ball1Rect)
        screen.blit(ball2, ball2Rect)
        pygame.display.flip()

