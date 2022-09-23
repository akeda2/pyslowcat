#!/usr/bin/python3
from ast import Try
import os
import time
import sys

path = './'

# mSec to sleep between printed lines
SOURCE = 100
if len(sys.argv) > 1:
	SOURCE = sys.argv[1]

SLEEPTIME = int(SOURCE) / 1000
#files = os.listdir(path)
while True:
    try:
        for root, directories, files in os.walk(path, topdown=False):
            for name in files:
                if not name.startswith('.'):
                    try:
                        with open(str(os.path.join(root, name)), 'r') as f: 
                            #print(f.read())
                            while True:
                                next_line = f.readline()
                                if not next_line:
                                    break;
                                #print(next_line.strip("\n"))
                                for char in next_line:
                                    print(char, end='', flush=True)
                                    time.sleep(0.005)
                                time.sleep(SLEEPTIME)
                            f.close()
                    except:
                        pass
    except KeyboardInterrupt:
        #raise SystemExit
        sys.exit()
            #print(os.path.join(root, name))
        #for name in directories:
        #	print(os.path.join(root, name))

