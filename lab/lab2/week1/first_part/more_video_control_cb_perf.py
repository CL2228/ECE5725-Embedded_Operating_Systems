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


def GPIO17_callback(channel):
    cmd = 'echo "pause" > /home/pi/0916/test_fifo'
    subprocess.check_output(cmd, shell=True)

def GPIO22_callback(channel):
    cmd = 'echo "seek 10" > /home/pi/0916/test_fifo'
    subprocess.check_output(cmd, shell=True)

def GPIO23_callback(channel):
    cmd = 'echo "seek -10" > /home/pi/0916/test_fifo'
    subprocess.check_output(cmd, shell=True)


# def GPIO27_callback(channel):
#     cmd = 'echo "quit" > /home/pi/0916/test_fifo'
#     print(subprocess.check_output(cmd, shell=True))


def GPIO26_callback(channel):
    cmd = 'echo "seek 30" > /home/pi/0916/test_fifo'
    subprocess.check_output(cmd, shell=True)

def GPIO19_callback(channel):
    cmd = 'echo "seek -30" > /home/pi/0916/test_fifo'
    subprocess.check_output(cmd, shell=True)



GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback, bouncetime=300)
GPIO.add_event_detect(22, GPIO.FALLING, callback=GPIO22_callback, bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=GPIO23_callback, bouncetime=300)
# GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO27_callback, bouncetime=300)
GPIO.add_event_detect(19, GPIO.FALLING, callback=GPIO19_callback, bouncetime=300)
GPIO.add_event_detect(26, GPIO.FALLING, callback=GPIO26_callback, bouncetime=300)

try:
    time.sleep(10)
    # cmd = 'echo "quit" > /home/pi/0916/test_fifo'
    # subprocess.check_output(cmd, shell=True)
    # GPIO27_callback(channel)
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()






