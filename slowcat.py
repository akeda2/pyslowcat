#!/usr/bin/python3
from ast import Try
import os
import time
import sys
import argparse



parser = argparse.ArgumentParser(description="slowcat - slow concatenation",
                                  formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#parser.add_argument("filename", default=None, nargs='?', help="Filename, if omitted - walk tree")
parser.add_argument('file', default=None, nargs='?', type=argparse.FileType('r'))
parser.add_argument("-c", "--char", action="store_true", help="Character mode")
parser.add_argument("-l", "--line", default=True, action="store_true", help="Line mode")
parser.add_argument("-s", "--sleep", default=51, type=int, help="Time to sleep between lines")
parser.add_argument("-p", "--pace", default=0.003, type=float, help="Character-mode pace")
parser.add_argument("-L", "--loop", default=False, action="store_true", help="Loop contents")
args = parser.parse_args()
config = vars(args)
print("slowcat - arguments:")
print(config)



#if args.filename:
#if not args.file:
    #path = args.filename
    #path = args.file
#else:
#    path = './'

#print(path)
# mSec to sleep between printed lines
#SOURCE = 50
#if len(sys.argv) > 1:
#	SOURCE = sys.argv[1]

time.sleep(2)
#SLEEPTIME = int(SOURCE) / 1000
SLEEPTIME = args.sleep / 1000
#files = os.listdir(path)
def onefile():
    while True:
        next_line = args.file.readline()
        if not next_line:
            break;
            #exit()
        if args.line:
            print(next_line.strip("\n"))
        elif args.char:
            for char in next_line:
                print(char, end='', flush=True)
                time.sleep(args.pace)
                time.sleep(0.003)
        if args.line and args.sleep == 51:
            time.sleep(SLEEPTIME*2)
        else:
            time.sleep(SLEEPTIME)
    #args.file.close()
#exit()

def oldshit():
#    if args.filename:
#if args.file:
    try:
        with open((args.filename), 'r') as f:
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
                if args.line and args.sleep == 51:
                    time.sleep(SLEEPTIME*2)
                else:
                    time.sleep(SLEEPTIME)
            f.close()
    except:
        pass
    exit()

def alltree():
#    while True:
    try:
        for root, directories, files in os.walk(path, topdown=False):
            for name in files:
                print(name)
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
                                if args.line and args.sleep == 51:
                                    time.sleep(SLEEPTIME*2)
                                else:
                                    time.sleep(SLEEPTIME)
                            f.close()
                    except:
                        raise
    except:
        raise
try:
    if args.file:
        while True:
            args.file.seek(0)
            onefile()
            if not args.loop:
                print("END")
                break;
        args.file.close()
        #exit()
    else:
        while True:
            path = './'
            alltree()
            if not args.loop:
                print("END")
                break;
        #exit()
except KeyboardInterrupt:
        #raise SystemExit
        sys.exit()
            #print(os.path.join(root, name))
        #for name in directories:
        #	print(os.path.join(root, name))