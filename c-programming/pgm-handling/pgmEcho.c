/**************************************************/
/*pgmEcho.c is improved by following              */
/*1. seperated the main function to more functions*/
/*2. added variable to structure                  */
/* 3. use goto to prevent repeating code          */
/**************************************************/

/* library for I/O routines        */
#include <stdio.h>

/* library for memory routines     */
#include <stdlib.h>

#include "pgmStructure.h"

#include "pgmError.h"

#include "pgmReadAndWrite.h"

/***********************************/
/* main routine                    */
/*                                 */
/* CLI parameters:                 */
/* argv[0]: executable name        */
/* argv[1]: input file name        */
/* argv[2]: output file name       */
/* returns 0 on success            */
/* non-zero error code on fail     */
/***********************************/
int main(int argc, char **argv){ 
	/*memory allocated structure*/
	PGMImage *pgm = malloc(sizeof(PGMImage)); 
	structure(pgm); 
	/* main() */
	/* check for correct number of arguments */
	if (argc == 1){
		/* check if argument is 0*/
		/* return special message indicating the correct usage and return 0*/
		printf("Usage: %s inputImage.pgm outputImage.pgm", argv[0]); 
		/* return no error*/
		return EXIT_NO_ERRORS; 
	}
	if (argc != 3)	{
		/* wrong arg count */
		/* print an error message        */
		printf("ERROR: Bad Argument Count");
		/* and return an error code      */
		return EXIT_WRONG_ARG_COUNT;
	} /* wrong arg count */
	/*read file from .h file and return the value inside*/
	int return_read_file = readfile(pgm, argv[1]);
	/*if read file has no error then write file*/
	if(return_read_file == EXIT_NO_ERRORS){
		int return_write_file = writefile(pgm, argv[2]);
		if(return_write_file == EXIT_NO_ERRORS)
			printf("ECHOED");
		/*return value in write file*/
		free(pgm); 
		return return_write_file; 
	}
	else{
		/*else return error */
		return return_read_file;
	}
}
