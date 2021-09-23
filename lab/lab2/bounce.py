import pygame
import os
import cv2
import matplotlib.pyplot as plt











if __name__ == "__main__":

    size = width, height = 500, 400
    speed = [1, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    ball = pygame.image.load("test.png")
    ballRect = ball.get_rect()

    while True:
        ballRect = ballRect.move(speed)
        if ballRect.left < 0 or ballRect.right > width:
            speed[0] = -speed[0]
        if ballRect.top < 0 or ballRect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballRect)
        pygame.display.flip()


