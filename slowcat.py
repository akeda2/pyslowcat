#!/usr/bin/python3
from ast import Try
import os
import time
import sys
import argparse

path = './'

parser = argparse.ArgumentParser(description="slowcat - slow concatenation",
                                  formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-c", "--char", action="store_true", help="Character mode")
parser.add_argument("-l", "--line", action="store_true", help="Line mode")
parser.add_argument("-s", "--sleep", default=50, type=int, help="Time to sleep between lines")
parser.add_argument("-p", "--pace", default=0.003, type=float, help="Character-mode pace")
args = parser.parse_args()
config = vars(args)
print("slowcat - arguments:")
print(config)

# mSec to sleep between printed lines
#SOURCE = 50
#if len(sys.argv) > 1:
#	SOURCE = sys.argv[1]

time.sleep(2)
#SLEEPTIME = int(SOURCE) / 1000
SLEEPTIME = args.sleep / 1000
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
                                if args.line:
                                    print(next_line.strip("\n"))
                                elif args.char:
                                    for char in next_line:
                                        print(char, end='', flush=True)
                                        time.sleep(args.pace)
                                        time.sleep(0.003)
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

