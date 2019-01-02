CC = gcc

.PHONY: clean

candpy.so:candpy.o
	$(CC) -shared -o candpy.so candpy.o

candpy.o:candpy.c
	$(CC) -c candpy.c

clean:
	rm -f *.o *.so