#!/usr/bin/python3
from ast import Try
import os
import time
import sys
import argparse



parser = argparse.ArgumentParser(description="slowcat - slow concatenation",
                                  formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#parser.add_argument("filename", default=None, nargs='?', help="Filename, if omitted - walk tree")
parser.add_argument('file', default=None, nargs='?', type=argparse.FileType('r'), help="Filename or '-' for stdin. If omitted - walk tree")
parser.add_argument("-c", "--char", action="store_true", help="Character mode")
parser.add_argument("-l", "--line", default=True, action="store_true", help="Line mode")
parser.add_argument("-s", "--sleep", default=51, type=int, help="Time to sleep between lines")
parser.add_argument("-p", "--pace", default=0.003, type=float, help="Character-mode pace (sleep between chars)")
parser.add_argument("-L", "--loop", default=False, action="store_true", help="Loop contents")
args = parser.parse_args()
config = vars(args)
#print("slowcat - arguments:")
print(config)

if args.char:
    args.line = False

time.sleep(2)
SLEEPTIME = args.sleep / 1000
if args.line and args.sleep == 51:
    SLEEPTIME *= 2
 
exclude_prefixes = ('__', '.')

def onefile():
    try:
        while True:
            next_line = args.file.readline()
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
    except KeyboardInterrupt:
        raise SystemExit

def oldshit():
    try:
        with open((args.filename), 'r') as f:
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

def alltree():
    try:
        for root, directories, files in os.walk(path, topdown=True):
            directories[:] = [directories
                             for directories in directories
                             if not directories.startswith(exclude_prefixes)]
            files[:] = [files
                        for files in files
                        if not files.startswith(exclude_prefixes)]
            #if '.git' in directories:
            #    directories.remove('.git')
            for name in files:
                print(root,name, '\n')
                #if not name.startswith('.'):
                try:
                    if os.path.isfile(os.path.join(root, name)):
                        with open(str(os.path.join(root, name)), 'r') as f: 
                            #if os.path.isfile(f.name):
                                #print(f.name)
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
                    raise
    except KeyboardInterrupt:
        raise SystemExit
try:        
    if args.file:
        while True:
            if not args.file.name == '<stdin>':
                args.file.seek(0)
            onefile()
            if not args.loop or args.file.name == '<stdin>':
                print("END")
                break;
        args.file.close()
    else:
        while True:
            path = './'
            try:
                alltree()
                if not args.loop:
                    print("END")
                    break;
            except KeyboardInterrupt:
                raise SystemExit

except KeyboardInterrupt:
    raise SystemExit
    #exit()