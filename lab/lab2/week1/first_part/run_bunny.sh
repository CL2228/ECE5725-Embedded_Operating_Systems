~!/bin/bash




echo"run the bunny!"

sudo SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 mplayer -vo sdl -framedrop /home/pi/bigbuckbunny320p.mp4
