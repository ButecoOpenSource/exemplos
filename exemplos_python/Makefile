CC=gcc
CFLAGS=-shared -Wall -fPIC 
LDFLAGS=-L/Python27/libs -lpython2.7

all:
	$(CC) calculadoramodule.c $(CFLAGS) -o calculadoramodule.so -I/usr/include/python2.7 $(LDFLAGS)
