import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...
# setup piTFT buttons
#                        V need this so that button doesn't 'float'!
#GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # This causes a problem....
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(26, GPIO.IN)
GPIO.setup(19, GPIO.IN)


while True:
    time.sleep(1.0) # sleep a bit...
    print ("tick..")
    if ( not GPIO.input(17) ):
        print (" ")
        print ("Button 17 pressed....")
    if ( not GPIO.input(22) ):
        print (" ")
        print ("Button 22 pressed....")
    if ( not GPIO.input(23) ):
        print (" ")
        print ("Button 23 pressed....")
    if ( not GPIO.input(27) ):
        print (" ")
        print ("Button 27 pressed....")

    if ( not GPIO.input(26) ):
        print (" ")
        print ("Button 26 pressed....")
    if ( not GPIO.input(19) ):
        print (" ")
        print ("Button 19 pressed....")

