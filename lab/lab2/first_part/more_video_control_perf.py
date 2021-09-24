import RPi.GPIO as GPIO
import time
import subprocess


startT = time.time()

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
    # time.sleep(0.00002) # sleep a bit...
    #print "tick.."
    if ( not GPIO.input(17) ):
        #print (" ")
        #print "Button 17 pressed...."
        cmd = 'echo "pause" > /home/pi/0916/test_fifo'
        print (subprocess.check_output(cmd, shell=True))
    if ( not GPIO.input(22) ):
        #print (" ")
        #print "Button 22 pressed...."
        cmd = 'echo "seek 10" > /home/pi/0916/test_fifo'
        print (subprocess.check_output(cmd, shell=True))
    if ( not GPIO.input(23) ):
        #print (" ")
        #print "Button 23 pressed...."
        cmd = 'echo "seek -10" > /home/pi/0916/test_fifo'
        print (subprocess.check_output(cmd, shell=True))
    if ( not GPIO.input(27) ):
        #print (" ")
        #print "Button 27 pressed...."
        cmd = 'echo "quit" > /home/pi/0916/test_fifo'
        print (subprocess.check_output(cmd, shell=True))
        break;

    if ( not GPIO.input(26) ):      # move forward by 10seconds
        #print (" ")
        #print "Button 23 pressed...."
        cmd = 'echo "seek 30" > /home/pi/0916/test_fifo'
        print (subprocess.check_output(cmd, shell=True))
    if ( not GPIO.input(19) ):      # move forward by 10seconds
        #print (" ")
        #print "Button 23 pressed...."
        cmd = 'echo "seek -30" > /home/pi/0916/test_fifo'
        print (subprocess.check_output(cmd, shell=True))
    if time.time() - startT > 10:
        break






