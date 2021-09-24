"""
 Names: Chenghui Li,  Hehong Li
 NetIDs: cl2228,    hl778
 Lab1, 09/09/2021 & 09/16/2021
"""


import subprocess
import sys


x= sys.stdin.readline()

while x != "q\n":   # if input a q, break the while and quit the video

    if x == "p\n":  # if input a p, pause the video
        cmd = 'echo "' + "pause" + '" > /home/pi/0916/test_fifo'
        print(subprocess.check_output(cmd, shell=True))
        x = sys.stdin.readline()

cmd = 'echo "quit" > /home/pi/0916/test_fifo'
print (subprocess.check_output(cmd, shell=True))
