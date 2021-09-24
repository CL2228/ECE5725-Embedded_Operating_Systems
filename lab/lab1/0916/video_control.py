"""
 Names: Chenghui Li,  Hehong Li
 NetIDs: cl2228,    hl778
 Lab1, 09/09/2021 & 09/16/2021
"""



import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...
# setup piTFT buttons
#

# set up GPIOs that we need on the piTFT screen
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    time.sleep(1.0)  # time interval
    #print "tick.."
    if ( not GPIO.input(17) ):
        #print "Button 17 pressed...., pause the video"
        cmd = 'echo "pause" > /home/pi/0916/test_fifo'
        print (subprocess.check_output(cmd, shell=True))
    if ( not GPIO.input(22) ):
        #print "Button 22 pressed...., fast forward the video"
        cmd = 'echo "seek 10" > /home/pi/0916/test_fifo'
        print (subprocess.check_output(cmd, shell=True))
    if ( not GPIO.input(23) ):
        #print "Button 23 pressed...., backward the video"
        cmd = 'echo "seek -10" > /home/pi/0916/test_fifo'
        print (subprocess.check_output(cmd, shell=True))
    if ( not GPIO.input(27) ):
        #print (" ") 
        #print "Button 27 pressed...., quit the video"
        cmd = 'echo "quit" > /home/pi/0916/test_fifo'
        print (subprocess.check_output(cmd, shell=True))
        break
