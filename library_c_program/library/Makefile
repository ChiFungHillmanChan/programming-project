
# code details

EXE = ./bin/library
SRC= main.c library.c librarian.c user.c utility.c

# generic build details

CC=      gcc
CFLAGS= -std=c99 -Wall
CLINK= 

# compile to object code

OBJ= $(SRC:.c=.o)

.c.o:
	$(CC) $(CFLAGS) -c -o $@ $<

# build executable: type 'make'

$(EXE): $(OBJ)
	$(CC) $(OBJ) $(CLINK) -o $(EXE) 

# clean up and remove object code and executable: type 'make clean'

clean:
	rm -f $(OBJ) $(EXE)

# dependencies

main.o:      main.c library.h libraryStructures.h
library.o:   library.c library.h librarian.h user.h utility.h libraryStructures.h
librarian.o: librarian.c librarian.h libraryStructures.h
user.o:      user.c user.h libraryStructures.h
utility.o:   utility.c utility.h 

