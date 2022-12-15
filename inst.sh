#!/bin/bash

[ -f slowcat.py ] && sudo cp --remove-destination slowcat.py /usr/local/bin/slowcat && echo "Done" || echo "FAIL!"