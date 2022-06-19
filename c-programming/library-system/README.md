# C Programming Projects
By Hillman Chan

## Directory: library 
Directory library contains:
- .c files x 5: main.c, user.c, utility.c, librarian.c, library.c
- .h files x 5: libraryStructure.h, user.h, utillirt.h, librarian.h. library.c
- bin directory with books.txt contain books
- Makefile

Run function:
1. Go To library directory to stary the program using 
```bash
make
```
2. Run the program by using 
```bash
cd bin
./library books.txt
```

3. This program has two mode: user mode and librarian mode. You can log in by user of librarian.

- 3.1 User: User can borrow maximum 4 books from library. After borrowed books, they have to return it back to library.

- 3.2 Librarian: Librarian can check all the books and the borrowed books in it. 

4. Exit the program by option EXIT and clear the program by
```bash
make clean
```

