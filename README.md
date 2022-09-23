# pyslowcat

```
usage: slowcat [-h] [-c] [-l] [-s SLEEP] [-p PACE] [-L] [file]

slowcat - slow concatenation

positional arguments:
  file                  Filename or '-' for stdin. If omitted - walk tree (default: None)

options:
  -h, --help            show this help message and exit
  -c, --char            Character mode (default: False)
  -l, --line            Line mode (default: True)
  -s SLEEP, --sleep SLEEP
                        Time to sleep between lines (default: 51)
  -p PACE, --pace PACE  Character-mode pace (sleep between chars) (default: 0.003)
  -L, --loop            Loop contents (default: False)

```
