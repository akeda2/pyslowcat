# pyslowcat

```
usage: slowcat [-h] [-c] [-l] [-s SLEEP] [-p PACE] [-L] [-b] [file]

slowcat - slow concatenation

positional arguments:
  file                  Filename or '-' for stdin. If omitted - walk tree
                        (default: None)

optional arguments:
  -h, --help            show this help message and exit
  -c, --char            Character mode (default: False)
  -l, --line            Line mode (default: True)
  -s SLEEP, --sleep SLEEP
                        Time to sleep between lines (default: 51)
  -p PACE, --pace PACE  Character-mode pace (sleep between chars) (default:
                        0.003)
  -L, --loop            Loop contents (default: False)
  -b, --bell            Bell sound on newline (default: False)
```
###Examples:
```
Follow syslog with a bell on each newline:
tail -f -n 10 /var/log/syslog | slowcat -cb -

Semi-slowly loop contents of directory tree line for line:
slowcat -l 100 -L
```
