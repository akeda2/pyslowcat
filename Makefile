# slowcat.py Makefile
# 

all: slowcat del
# readme

# Create slowcat executable
slowcat:
	pyinstaller --clean slowcat.py -F
	mv dist/slowcat .

# Remove files created by pyinstaller
del:
	rm -rf ./dist/ ./build/ ./*.spec ./*.pyc ./*.log slowcat.spec dist/

# Clear pyinstall cache and delete file
clean:
	#pyinstaller --clean slowcat.py
	rm -rf ./dist/ ./build/ ./*.spec ./*.pyc ./*.log slowcat.spec dist/ slowcat

PREFIX ?= /usr/local
BINDIR ?= $(PREFIX)/bin

install:
	mkdir -p $(DESTDIR)$(BINDIR)
	install -m755 slowcat $(DESTDIR)$(BINDIR)/slowcat
