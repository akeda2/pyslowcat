#!/bin/bash

[ -f slowcat.py ] && sudo ln -s $(realpath slowcat.py) /usr/local/bin/slowcat && echo "Done"