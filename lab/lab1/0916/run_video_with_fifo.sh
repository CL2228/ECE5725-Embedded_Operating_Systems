#!/bin/bash

echo"haha"


sudo SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1  mplayer -vo sdl -framedrop -input file=/home/pi/0916/video_fifo /home/pi/bigbuckbunny320p.mp4
