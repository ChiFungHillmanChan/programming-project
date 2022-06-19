#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "utility.h"

////
// Utility functions to handle "safer" string input
//

// DONT ALTER THESE FUNCTIONS

// read in a line of text and convert to an integer option

int optionChoice( void ) {
    int option = -1;
    char line[80];

    // read in the current line as a string
    fgets(line,80,stdin);

    // atoi() converts string to integer, returns 0 if could not convert
    option = (int)atoi(line);

    return option;
}

// remove newline character from the fgets() input

void removeNewLine(char* string) {

    size_t length = strlen(string);

    if((length > 0) && (string[length-1] == '\n')) {
        string[length-1] ='\0';
    }
    return;
}
