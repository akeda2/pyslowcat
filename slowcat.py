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

# If we choose character mode, list line mode as False:
if args.char:
    args.line = False
# Print config and sleep for n seconds:
#print(config)
#time.sleep(2)

# From mS to S:
SLEEPTIME = args.sleep / 1000
# 102 mS is default for line mode, we are using 51*2 and using 51 for character mode:
if args.line and args.sleep == 51:
    SLEEPTIME *= 2
 
# We don't want to show hidden and garbage files:
exclude_prefixes = ('__', '.')

# Sanitize TTY:
def ttysane():
    if platform.system() != "Windows":
        os.system('stty sane')

# Use argparse inbuilt file reader for single files:
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
                            print(next_line, end='', flush=True)
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

# Use os.walk with with open for recursive tree mode:
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
                                            #print(next_line.strip("\n"))
                                            print(next_line, end='', flush=True)
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
                #print("END")
                break;
        args.file.close()
    else:
        while True:
            path = './'
            try:
                alltree()
                if not args.loop:
                    #print("END")
                    break;
            except KeyboardInterrupt:
                ttysane()
                raise SystemExit

except KeyboardInterrupt:
    ttysane()
    raise SystemExit
    #exit()