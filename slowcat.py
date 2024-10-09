#!/usr/bin/env python3
import os
import time
import argparse
import platform
import sys




# Sanitize TTY:
def ttysane():
    if platform.system() != "Windows":
        os.system('stty sane')


def process_file(file_obj, args, SLEEPTIME):
    """Process and print the content of a file based on the provided arguments."""
    try:
        for next_line in file_obj:
            if args.bell:
                print('\a', end='', flush=True)
            if args.char:
                for char in next_line:
                    print(char, end='', flush=True)
                    time.sleep(args.pace)
            else:
                print(next_line, end='', flush=True)
                time.sleep(SLEEPTIME)
    except KeyboardInterrupt:
        ttysane()
        sys.exit()

# Use argparse inbuilt file reader for single files:
def onefile(args,SLEEPTIME):

    """Handle a single file or stdin."""
    file_name = args.file.name
    if file_name == '<stdin>' or os.path.isfile(file_name):
        while True:
            if file_name != '<stdin>':
                args.file.seek(0)
            process_file(args.file, args, SLEEPTIME)
            if not args.loop or file_name == '<stdin>':
                break
        args.file.close()
    else:
        print(f"{file_name}: Not a file!")

    """ try:
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
        sys.exit(); """

# Use os.walk with with open for recursive tree mode:
def alltree(args,SLEEPTIME):
    """Walk through the directory tree and process files."""
    exclude_prefixes = ('__', '.')
    path = './'
    try:
        for root, directories, files in os.walk(path, topdown=True):
            directories[:] = [d for d in directories if not d.startswith(exclude_prefixes)]
            files[:] = [f for f in files if not f.startswith(exclude_prefixes)]
            for name in files:
                file_path = os.path.join(root, name)
                print(f"\nProcessing {file_path}\n")
                try:
                    with open(file_path, 'r', errors='replace') as f:
                        process_file(f, args, SLEEPTIME)
                except OSError:
                    print(f"Could not read file: {file_path}")
            if not args.loop:
                break
    except KeyboardInterrupt:
        ttysane()
        sys.exit()

    """ try:
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
                            #f.close()
                        except OSError:
                            print("Could not read file")
                            pass
                except:
                    raise
    except KeyboardInterrupt:
        ttysane()
        sys.exit() """


def main():

    parser = argparse.ArgumentParser(
        description="slowcat - slow concatenation",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--char", action="store_true", help="Character mode")
    group.add_argument("-l", "--line", action="store_true", help="Line mode (default)", default=True)
    parser.add_argument('file', default=None, nargs='?', type=argparse.FileType('r', errors='replace'),
                        help="Filename or '-' for stdin. If omitted, walk tree")
    parser.add_argument("-s", "--sleep", type=int, help="Time to sleep between lines (ms)")
    parser.add_argument("-p", "--pace", default=0.003, type=float, help="Character-mode pace (sleep between chars)")
    parser.add_argument("-L", "--loop", action="store_true", help="Loop contents")
    parser.add_argument("-b", "--bell", action="store_true", help="Bell sound on newline")
    args = parser.parse_args()

    # Set default sleep times
    if args.sleep is None:
        args.sleep = 102 if args.line else 51
    SLEEPTIME = args.sleep / 1000

    """ parser = argparse.ArgumentParser(description="slowcat - slow concatenation",
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
    exclude_prefixes = ('__', '.') """

    try:
        if args.file:
            onefile(args, SLEEPTIME)
        else:
            alltree(args, SLEEPTIME)
    except KeyboardInterrupt:
        ttysane()
        sys.exit()

    """ try:        
        if args.file:
            while True:
                if not args.file.name == '<stdin>':
                    args.file.seek(0)
                onefile(args,int: SLEEPTIME)
                if not args.loop or args.file.name == '<stdin>':
                    #print("END")
                    break;
            args.file.close()
        else:
            while True:
                path = './'
                try:
                    alltree(args,int: SLEEPTIME)
                    if not args.loop:
                        #print("END")
                        break;
                except KeyboardInterrupt:
                    ttysane()
                    sys.exit()


    except KeyboardInterrupt:
        ttysane()
        sys.exit()
        #exit() """

if __name__ == "__main__":
    main()