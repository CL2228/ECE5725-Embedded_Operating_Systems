import subprocess
import sys


x= sys.stdin.readline()

while x != "q\n":
    if x == " \n":
        x = "pause"
        print(x)
        cmd = 'echo "' + x + '" > /home/pi/0916/test_fifo' 
        x = sys.stdin.readline()

cmd = 'echo "quit" > /home/pi/0916/test_fifo'
print subprocess.check_output(cmd, shell=True)
