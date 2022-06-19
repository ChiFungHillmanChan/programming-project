/* library for I/O routines        */
#include <stdio.h>

/* library for memory routines     */
#include <stdlib.h>

#include "pgmStructure.h"
#include "pgmError.h"
#include "pgmReadAndWrite.h"
#include "pgmConvert.h"

int main(int argc, char **argv){
    /*memory allocated structure*/
	PGMImage *pgm = malloc(sizeof(PGMImage)); 
	structure(pgm); 
	int checkerror = 0; 
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
    checkerror = pgma2b(pgm, argv[1]); 
	/*return error if check error is not success*/
	if(checkerror != 0)
        return checkerror;  
	/*write file if no error in reading*/
	checkerror = writefile(pgm, argv[2]); 
	/*return error if check error is not success*/
	if(checkerror != 0)
		return checkerror; 
	/* all success and free the pointer */
	printf("CONVERTED");
	free(pgm); 
    return EXIT_NO_ERRORS; 
}
