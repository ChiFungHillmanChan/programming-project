/* library for I/O routines        */
#include <stdio.h>

/* library for memory routines     */
#include <stdlib.h>

#include "pgmStructure.h"

#include "pgmError.h"

#include "pgmReadAndWrite.h"

#include "pgmConvert.h"

#include "pgmAssemble.h"

/***********************************/
/* main routine                    */
/*                                 */
/* CLI parameters:                 */
/* argv[0]: executable name        */
/* argv[1]: output file name       */
/* argv[2]: output file row number */
/* argv[2]: output file col number */
/* argv[3i + 1]: input file row    */
/* argv[3i + 2]: input file col    */
/* argv[3i + 3]: input file name   */
/*                                 */
/* returns 0 on success            */
/* non-zero error code on fail     */
/***********************************/

int main(int argc, char **argv){ 
   
    int error_number = 0;
	/* main() */
	/* check for correct number of arguments */
	if (argc == 1){
		/* check if argument is 0 */
		/* return special message indicating the correct usage and return 0 */
		printf("Usage: %s outputImage.pgm width height (row column inputImage.pgm)+", argv[0]); 
		/* return no error*/
		return EXIT_NO_ERRORS; 
	}
	if (( argc - 1 ) % 3 != 0){
		/* wrong arg number */
		/* print an error message        */
		printf("ERROR: Bad Argument Count");
		/* and return an error code      */
		return EXIT_WRONG_ARG_COUNT;
	} /* wrong arg count */

    /* memory allocated structure */
	PGMImage *pgm = malloc(sizeof(PGMImage)); 
	structure(pgm);

    /* get the width and height for the output file */
    pgm->width = atoi(argv[2]);
	pgm->height = atoi(argv[3]);

    if(!atoi(argv[2]) || ! atoi(argv[3]) || atoi(argv[2]) < 1 || atoi(argv[3]) < 1){
        printf("ERROR: Miscellaneous (The Assemble file width and height must be a positive integer)");
        return MISCELLANEOUS;
    }
    /* allocate the data pointer */   
    pgm->imageData = (unsigned char **)malloc(pgm->height * sizeof(*pgm->imageData));
    for (int i = 0; i < pgm->height; i++){
        pgm->imageData[i] = (unsigned char *) malloc(pgm->width * sizeof(unsigned char));
        /* check the error for imageData */
        int checkerror_return = check_imageData(argv[1], pgm->imageData[i]);
        if (checkerror_return != 0)
            return checkerror_return;  
    } 

	for (int i = 1; i < (((argc - 4)/ 3) + 1); i++){
        /* use for loop to read all the file */
		error_number = Assemble_File_Read(pgm, argv[3*i+3], atoi(argv[3*i+1]), atoi(argv[3*i+2]));
        /* return the error gets, else continue */
		if(error_number!= EXIT_NO_ERRORS){
			free(pgm);
			return error_number;
        }
	}
    /* write the file if no error in reading all the file */
	error_number = writefile(pgm, argv[1]);
    /* return error gets */
	if (error_number != EXIT_NO_ERRORS){
		free(pgm); 
        return error_number;
	}
    /*return value in assemble file*/
    /* success assembling   */
    printf("ASSEMBLED");
    /* free the pointer and return */
    free(pgm); 
    return EXIT_NO_ERRORS;  
}

int Assemble_File_Read(PGMImage *pgm, const char *filename, int row, int col) {
    /* this variable is to check the function returns value*/
    int checkerror_return = 0; 
    /* these two variable is for getting the row and column started */
	int row_for_file; 
	int col_for_file; 
    pgm->magic_Number = (unsigned short *) pgm->magic_number; 
    /* now start reading in the data         */
    /* try to open the file for text I/O     */
    /* in ASCII mode b/c the header is text  */
    FILE *pgmFile = fopen(filename, "r");

    /* failed to open file*/
    checkerror_return = check_file(pgmFile, filename); 
    if (checkerror_return != 0)
        return checkerror_return; 
    /* read in the magic number              */
    pgm->magic_number[0] = getc(pgmFile);
    pgm->magic_number[1] = getc(pgmFile);

    /* P2 == ASCII code file, P5 == binary code file*/
    checkerror_return = check_magic_number(pgm, filename, pgm->magic_Number, pgm->magic_number[1]);
    if(checkerror_return != 0)
        return checkerror_return; 
    
    /* scan whitespace if present            */
    int scanCount = fscanf(pgmFile, " ");

    /* check for a comment line              */
    char nextChar = fgetc(pgmFile);

    if (nextChar == '#'){ 
        /* comment line                */
        pgm->commentLine = (char *) malloc(MAX_COMMENT_LINE_LENGTH + 2); 
        /* fgets() reads a line          */
        /* capture return value          */
        char *commentString = fgets(pgm->commentLine, MAX_COMMENT_LINE_LENGTH + 2, pgmFile);

        checkerror_return = check_commentString(pgm, filename, commentString);
        if (checkerror_return != 0){
            return checkerror_return; 
        }
    } /* comment line */
    else{
        /* not a comment line */
        /* put character back            */
        ungetc(nextChar, pgmFile);
    } /* not a comment line */

    /* read in width, height, grays          */
    /* whitespace to skip blanks             */
    scanCount = fscanf(pgmFile, " %u %u %u", &row_for_file, &col_for_file, &(pgm->maxGray));

    checkerror_return = check_scanCount(filename, scanCount, row_for_file, col_for_file, pgm->maxGray);
    if (checkerror_return != 0)
        return checkerror_return;
    /*check error*/ 
    
    /* this variable is to check if there is extre data */ 
    int checktooMuchData = -1;
    /* pointer for efficient read ASCII code */
    if(pgm->magic_number[1] == '2'){
        /* the two for loop is used to read the data */
        /* it will store to the specific row and column required */
        for (int i = row; i < row+row_for_file; i++){
            for (int j = col; j < col+col_for_file; j++){
                int grayValue = -1;
                int scanCount =  fscanf(pgmFile, "%u", &grayValue);
                /* check error */
                checkerror_return = check_grayValue(filename, grayValue, scanCount);
                if (checkerror_return != 0)
                    return checkerror_return; 
                /* save to imageData if no error */
                pgm->imageData[i][j] = (unsigned char) grayValue;
            }
        }
        /* check if there is too much data */
        int scanCount = fscanf(pgmFile, "%u", &checktooMuchData);
        if(scanCount > 0){
            printf("ERROR: Bad Data (%s)", filename);
            return BAD_DATA;
        }
    }
    /*read as binary*/
    else if (pgm->magic_number[1] == '5'){
        fgetc(pgmFile);      //this will read the empty line
        /* the two for loop is used to read the data */
        /* it will store to the specific row and column required */
        for (int i = 0; i < row+row_for_file + 1; i++){
            for(int j = 0; j < col+col_for_file + 1; j++){
                int scanCount = fread(&pgm->imageData[i][j], sizeof(unsigned char),1, pgmFile);
                if(scanCount != 1){
                printf("ERROR: Bad Data (%s)", filename);
                    return BAD_DATA;
                }
            }
        }
        /* check if there is too much data */
        if(fscanf(pgmFile, "%u", &checktooMuchData) > 0){
            printf("ERROR: Bad Data (%s)", filename);
            return BAD_DATA;
        }
    }  
    // /*close file and return 0 as no error */
    fclose(pgmFile);
	return checkerror_return; 
}