"""
 Names: Chenghui Li,  Hehong Li
 NetIDs: cl2228,    hl778
 Lab1, 09/09/2021 & 09/16/2021
"""


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...
# setup piTFT buttons
#                        V need this so that button doesn't 'float'!

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    time.sleep(1.0) # time interval
    print ("tick..")
    if ( not GPIO.input(17) ):      # 17 detected
        print (" ") 
        print ("Button 17 pressed....")
    if ( not GPIO.input(22) ):      # 22 detected
        print (" ") 
        print ("Button 22 pressed....")
    if ( not GPIO.input(23) ):      # 23 detected
        print (" ") 
        print ("Button 23 pressed....")
    if ( not GPIO.input(27) ):      # 27 detected
        print (" ") 
        print ("Button 27 pressed....")
        break
