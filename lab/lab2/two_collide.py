import pygame



if __name__ == "__main__":
    size = width, height = 320, 240
    speed1 = [1, 2]
    speed2 = [2, 1]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    ball1 = pygame.image.load("berkeley.jpg")
    ball1Rect = ball1.get_rect()
    ball2 = pygame.image.load("test.png")
    ball2Rect = ball2.get_rect()


    while True:
        ball1Rect = ball1Rect.move(speed1)
        ball2Rect = ball2Rect.move(speed2)

        if ball1Rect.left < 0 or ball1Rect.right > width:
            speed1[0] = -speed1[0]
        if ball1Rect.top < 0 or ball1Rect.bottom > height:
            speed1[1] = -speed1[1]

        if ball2Rect.left < 0 or ball2Rect.right > width:
            speed2[0] = -speed2[0]
        if ball2Rect.top < 0 or ball2Rect.bottom > height:
            speed2[1] = -speed2[1]

        screen.fill(black)
        screen.blit(ball1, ball1Rect)
        screen.blit(ball2, ball2Rect)
        pygame.display.flip()