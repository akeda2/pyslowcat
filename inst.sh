#!/bin/bash

PREFIX ?= /usr/local
BINDIR ?= $(PREFIX)/bin
mkdir -p $(DESTDIR)$(BINDIR)
[[ -f slowcat.py ]] && { install -m755 slowcat $(DESTDIR)$(BINDIR)/slowcat && echo "installed!" || echo "FAILED!"; } || echo "slowcat.py not found...!"
#[ -f slowcat.py ] && sudo cp --remove-destination slowcat.py /usr/local/bin/slowcat && echo "Done" || echo "FAIL!"