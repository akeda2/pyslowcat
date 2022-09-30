#!/usr/bin/python3
from ast import Try
import os
import time
import sys
import argparse
import platform



parser = argparse.ArgumentParser(description="slowcat - slow concatenation",
                                  formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#parser.add_argument("filename", default=None, nargs='?', help="Filename, if omitted - walk tree")
parser.add_argument('file', default=None, nargs='?', type=argparse.FileType('r'), help="Filename or '-' for stdin. If omitted - walk tree")
parser.add_argument("-c", "--char", action="store_true", help="Character mode")
parser.add_argument("-l", "--line", default=True, action="store_true", help="Line mode")
parser.add_argument("-s", "--sleep", default=51, type=int, help="Time to sleep between lines")
parser.add_argument("-p", "--pace", default=0.003, type=float, help="Character-mode pace (sleep between chars)")
parser.add_argument("-L", "--loop", default=False, action="store_true", help="Loop contents")
parser.add_argument("-b", "--bell", default=False, action="store_true", help="Bell sound on newline")
args = parser.parse_args()
config = vars(args)
print(config)

if args.char:
    args.line = False

time.sleep(2)
SLEEPTIME = args.sleep / 1000
if args.line and args.sleep == 51:
    SLEEPTIME *= 2
 
exclude_prefixes = ('__', '.')
def ttysane():
    if platform.system() != "Windows":
        os.system('stty sane')
def onefile():
    try:
        if os.path.isfile(args.file.name) or args.file.name == '<stdin>':
            try:
                while True:
                    try:
                        next_line = args.file.readline()
                        if not next_line:
                            break;
                        if args.line:
                            if args.bell:
                                print('\a', end='', flush=True)
                            print(next_line.strip("\n"))
                        elif args.char:
                            if args.bell:
                                print('\a', end='', flush=True)
                            for char in next_line:
                                print(char, end='', flush=True)
                                time.sleep(args.pace)
                        time.sleep(SLEEPTIME)
                    except KeyboardInterrupt:
                        ttysane()
                        raise SystemExit
                    except:
                        break;
            except OSError:
                print(args.file.name,": Could not read file")
                pass
        else:
            print(args.file.name,": Not a file!")
    except KeyboardInterrupt:
        ttysane()
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
            
            for name in files:
                print(root+'/'+name)
            for name in files:
                print('\n',root+'/'+name, '\n')
                try:
                    if os.path.isfile(os.path.join(root, name)):
                        try:
                            with open(str(os.path.join(root, name)), 'r') as f: 
                                while True:
                                    try:
                                        next_line = f.readline()
                                        if not next_line:
                                            break;
                                        if args.line:
                                            print(next_line.strip("\n"))
                                        elif args.char:
                                            for char in next_line:
                                                print(char, end='', flush=True)
                                                time.sleep(args.pace)
                                    except KeyboardInterrupt:
                                        ttysane()
                                        raise SystemExit
                                    except:
                                        break;
                                    time.sleep(SLEEPTIME)
                            f.close()
                        except OSError:
                            print("Could not read file")
                            pass
                except:
                    raise
    except KeyboardInterrupt:
        ttysane()
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
                ttysane()
                raise SystemExit

except KeyboardInterrupt:
    ttysane()
    raise SystemExit
    #exit()