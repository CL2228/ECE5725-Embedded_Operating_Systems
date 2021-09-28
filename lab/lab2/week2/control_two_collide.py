import os
import pygame






if __name__ == "__main__":

    # un-comment these statements when using monitor!
    # os.putenv('SDL_VIDEODRIVER', 'fbcon')       # display on piTFT
    # os.putenv('SDL_FBDEV', '/dev/fb1')
    # os.putenv('SDL_MOUSEDRV', 'TSLIB')          # Track mouse clicks on piTFT
    # os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')


    # True for monitor, False for piTFT
    pygame.mouse.set_visible(True)
