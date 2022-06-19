#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "libraryStructures.h"
#include "library.h"
#include "user.h"
#include "librarian.h"
#include "utility.h"

////
// Code module for main library menu and file management
// Reads the book and initialises the problem data

// Initialise library data
// Input:
// bookfile - name of book file
// theLibrary - library data structure

void initLibrary( char *bookFile, Library *theLibrary ) {

  theLibrary->maxBooks = 12;
  theLibrary->maxBorrowed = 4;
  // TO DO :

  // dynamically allocate the bookList array for storing books
  theLibrary->bookList = (Book*)malloc ( sizeof (Book) );
  // check the book file exists
  // use the error message and exit the program if it does not
  // open it if it exists
  FILE *books = fopen(bookFile, "r");
  if (books == NULL)
  {
    printf("Error\nBook file does not exist: %s\n",bookFile);
    exit(0);
  }
  // use the readBooks function to read in the file and add the book records into the bookList array
  theLibrary->numBooks = readBooks(books, theLibrary->bookList);
  // remember to close the file
  fclose(books);
  // Initialise the User data
  return;
}

// Read in book file and create the books data structure
// the book file is in a fixed format:
// * book author
// * book title
// * blank line
// Input:
//   books - file pointer to text input file
//   bookList - alocated array for storing Book structures
// Output:
//   numBooks - number of books read

int readBooks( FILE *books, Book *bookList ) {

  int numBooks = 0;
  // TO DO:
  // read from the book file pointer
  // assign values to a Book structure in the bookList array for each complete record
  char space[40];
  while(!feof(books))
  {
    fgets(bookList[numBooks].title, sizeof(bookList->title), books);
    removeNewLine(bookList[numBooks].title);

    fgets(bookList[numBooks].author, sizeof(bookList->author), books);
    removeNewLine(bookList[numBooks].author);

    fgets(space, 40, books);

    numBooks++;
  }

  //method 2*
  //while(fgets(space, 40, books) != NULL)
  //{
    //if (strcmp(space, "\n")!= 0)
    //{
      //removeNewLine(space);
      //strncpy(bookList[numBooks].title, space, 40);
      //fgets(bookList[numBooks].author, 40, books);
      //removeNewLine(bookList[numBooks].author);
      //numBooks++;
    //}
  //}
  
  // read data until the file ends
  return numBooks;
}

// Free any allocated library data
// Input:
// theLibrary - library data structure

void exitLibrary( Library *theLibrary ) {

  // TO DO:
  // free the allocated lists
  free (theLibrary->bookList);
  return;
}

// DO NOT ALTER THIS FUNCTION
// Library menu system

void libraryCLI( char *bookFile ) {
    int libraryOpen = 1;
    int option;

    // create the library structure
    Library *theLibrary = (Library *)malloc( sizeof(Library) );

    initLibrary( bookFile, theLibrary );

    while( libraryOpen ){
        printf("\n Main menu options\n 1 User login\n 2 Librarian login\n 3 Exit system\n Choice:");
        option = optionChoice();

        if( option == 1 ) {
            printf("\nUser login\n");
            userCLI( theLibrary );
        }
        else if( option == 2 ) {
            printf("\nLibrarian login\n");
            librarianCLI( theLibrary );
        }
        else if( option == 3 ) {
            libraryOpen = 0;
            printf("\nClosing\n");
        }
        else
            printf("\nUnknown option\n");
    }

    exitLibrary( theLibrary );

    // free the library structure
    free( theLibrary );

    return;
}
