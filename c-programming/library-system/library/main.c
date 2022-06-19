
// Name: Chi Fung Hillman Chan
// Username: Chi Fung Hillman Chan
// Date started: 20/12/2021

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "libraryStructures.h"
#include "library.h"

////
// Code module for main()
// main function takes command line arguments
// and opens the library menu
// Input: book data filename via command line
// Usage: ./library books.txt

int main( int argc, char **argv )
{
    char bookFile[40];
    //TO DO :
    if (argc != 2)
    {
    // check that correct number of command line arguments are entered
    // use the error message
        printf("Error\nExpected use: ./library books.txt\n");
        return -1;
    }
    // exit the application if there is an error
    // assign command line value to filename string
    strcpy( bookFile, argv[1]);
    // DO NOT ALTER
    // start the system
    printf("\nIntialising library system!\n");
    libraryCLI( bookFile );
    printf("\nClosing library system!\n\n");
    return 0;
}
