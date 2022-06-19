#include <stdio.h>
#include <stdlib.h>

#include "libraryStructures.h"
#include "user.h"
#include "utility.h"

////
// Code module for the library user
// They can look for available books,
// borrow and return books

// List the books that are available to borrow
// Input
// bookList - the array of Book structures
// numBooks - the number of books

void listAvailableBooks( Book *bookList, int numBooks ) {

  // TO DO :
  // print out available books with format "list number - author - title" on each line
  printf("\n");
  for (int i = 0; i < numBooks; i++)
  {
    if (bookList[i].available >= 0)
    {
      printf("%d - %s - %s\n\n", i, bookList[i].title, bookList[i].author);
    }
  }
  return;
}

// Borrow a book
// Input
// theUser - user data structure
// bookList - the array of Book structures
// numBooks - the number of books
// maxBorrowed - max books we can borrow

void borrowBook( User *theUser, Book *bookList, int numBooks, int maxBorrowed ) {

  // TO DO :
  // For any error message you should return to the menu

  if (theUser->numBorrowed == 0) // set Book borrowed to NULL><
  {
    for (int i = 0; i < maxBorrowed; i++)
    {
      theUser->borrowed[i]= NULL;
    }
  }
  for (int i = 0; i < maxBorrowed; i++)
  {
    if (theUser->borrowed[i] != NULL && theUser->borrowed[i]->available > 0)
    {
      theUser->borrowed[i] = NULL;
    }
  }

  //for (int i = 0; i < maxBorrowed; i++) // set book after return to NULL><

  // check that the user can borrow a book
  if (theUser->numBorrowed == maxBorrowed)
  {
    printf("You have to return a book before you can borrow another\n");
    return;
  }
  // request the choice of book
  // message
  printf("Which book? (number):");
  int option = optionChoice();
  // check that the choice is valid
  // error messages
  if (option >= numBooks || option < 0)
  {
    printf("Error\nInvalid choice\n");
    return;
  }
  if (bookList[option].available < 0)
  {
    printf("Book is not available\n");
    return;
  }
  for (int i = 0; i < maxBorrowed; i++)
  {
    if (theUser->borrowed[i] == NULL)
    {
      theUser->borrowed[i] = &bookList[option];
      bookList[option].available = -1;
      theUser->borrowed[i]->available = -1;
      break;
    }
  }
  theUser->numBorrowed++;


  // borrow the book, update the data structures
  return;
}

// List books I have borrowed
// Input
// theUser - user data structure
// bookList - the array of Book structures
// maxBorrowed - max books we can borrow

void listMyBooks( User *theUser, Book *bookList, int maxBorrowed ) {

  // TO DO :

  // list my books in format "number - author - title"
  printf("\n");

  for (int i = 0; i < maxBorrowed ; i++)
  {
    if (theUser->borrowed[i] != NULL)
    {
      if(theUser->borrowed[i]->available < 0)
      {
        printf("%d - %s - %s\n\n", i, theUser->borrowed[i]->title , theUser->borrowed[i]->author);
      }
    }
  }
  return;
}

// Return a book
// Input
// theUser - user data structure
// bookList - the array of Book structures
// numBooks - the number of books
// maxBorrowed - max books we can borrow

void returnBook( User *theUser, Book *bookList, int numBooks, int maxBorrowed ) {

  // TO DO :
  // For any error message you should return to the menu
  // check that we have borrowed books
  // error message
  if (theUser->numBorrowed == 0)
  {
    printf("Error\nYou have not borrowed any books\n");
    return;
  }
  // request the choice of book
  // message
  printf("Which book? (number):");
  int option = optionChoice();
  // check the choice is valid
  // error messages
  if (option >= maxBorrowed||option < 0||theUser->borrowed[option] == NULL||theUser->borrowed[option]->available == 1)
  {
    printf("Error\nInvalid choice\n");
    return;
  }

  for (int i = 0; i < numBooks; i++)
  {
    if (theUser->borrowed[option]  == &bookList[i] )
    {
      bookList[i].available = 1;
      break;
    }
  }
  theUser->borrowed[option]->available = 1;
  theUser->numBorrowed --;
  // return the book and update data structures

  return;
}

// DO NOT ALTER THIS FUNCTION

// Menu system for library user

void userCLI( Library *theLibrary ) {
    int userLoggedIn = 1;
    int option;

    while( userLoggedIn ){
        printf("\n User options\n 1 List available books\n 2 Borrow book\n 3 Return book\n 4 Log out\n Choice:");
        option = optionChoice();

        if( option == 1 ) {
            printf("\nList available books:\n");
            listAvailableBooks( theLibrary->bookList, theLibrary->numBooks );
        }
        else if( option == 2 ) {
            printf("\nBorrow book from library:\n");
            listAvailableBooks( theLibrary->bookList, theLibrary->numBooks );
            borrowBook( &(theLibrary->theUser), theLibrary->bookList, theLibrary->numBooks, theLibrary->maxBorrowed );
        }
        else if( option == 3 ) {
            printf("\nReturn book from my list:\n");
            listMyBooks( &(theLibrary->theUser), theLibrary->bookList, theLibrary->maxBorrowed );
            returnBook( &(theLibrary->theUser), theLibrary->bookList, theLibrary->numBooks, theLibrary->maxBorrowed );
        }
        else if( option == 4 ) {
            userLoggedIn = 0;
            printf("\nLogging out\n");
        }
        else
            printf("\nUnknown option\n");
    }
    return;
}
