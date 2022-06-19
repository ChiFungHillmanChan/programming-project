/* library for I/O routines        */
#include <stdio.h>

/* library for memory routines     */
#include <stdlib.h>

#include "pgmStructure.h"

#include "pgmError.h"

#include "pgmReadAndWrite.h"

#include "pgmReduce.h"

/***********************************/
/* main routine                    */
/*                                 */
/* CLI parameters:                 */
/* argv[0]: executable name        */
/* argv[1]: input file name        */
/* argv[2]: an integer factor n    */
/* argv[3]: output file name       */
/* returns 0 on success            */
/* non-zero error code on fail     */
/***********************************/

int main(int argc, char **argv){ 
    /*memory allocated structure*/
	PGMImage *pgm = malloc(sizeof(PGMImage)); 
	structure(pgm); 
    int reducing_number = 0;
	/* main() */
	/* check for correct number of arguments */
	if (argc == 1){
		/* check if argument is 0*/
		/* return special message indicating the correct usage and return 0*/
		printf("Usage: %s inputImage.pgm reduction_factor outputImage.pgm", argv[0]); 
		/* return no error*/
		return EXIT_NO_ERRORS; 
	}
	if (argc != 4){
		/* wrong arg count */
		/* print an error message        */
		printf("ERROR: Bad Argument Count");
		/* and return an error code      */
		return EXIT_WRONG_ARG_COUNT;
	} /* wrong arg count */

    /* Use this function to read the file */
    /* read file if success */
    int return_read_file = readfile(pgm, argv[1]);
    /* return error if exist, else continue*/
    if(return_read_file != EXIT_NO_ERRORS)
        return return_read_file;

    /* check if the second argument line is number or not*/
    reducing_number = atoi(argv[2]); 
    /* if second argument is not a possitibe integer, return error */
    if( !reducing_number || reducing_number < 0){
        printf("ERROR: Miscellaneous (The reduction factor must be a possitive integer)");
        return MISCELLANEOUS;
    }
    /* Go to reduce file if no error in reading file */
    int return_reduce_file = ReduceFile(pgm, argv[3], reducing_number);
    /*return value in write file*/
    if(return_reduce_file != EXIT_NO_ERRORS)
        return return_reduce_file;
    /* success reducing */
    printf("REDUCED");
    /* free the pointer */
    free(pgm); 
    return return_reduce_file; 
}

int ReduceFile(PGMImage *pgm,  const char *filename, int reduce_number){
	/* open a file for reducing file             */
    /* this variable is to check the function returns value*/
    int checkerror_return = 0; 
    /* open file for writing */
    FILE *pgmFile = fopen(filename, "w");

    checkerror_return = check_outputfile(pgmFile, pgm, filename); 
    /* check if the file is writeable */
    if (checkerror_return != 0)
        return checkerror_return; 
    /* reduce the file width and height */
    int reduce_height = pgm->height/reduce_number;
    int reduce_width = pgm->width/reduce_number;
    /* for printing value */
    /* if the mod is not 0, the width or the height needs to add 1 */
    if(pgm->height % reduce_number != 0){
        reduce_height += 1;
    }
    if( pgm->width % reduce_number != 0){
        reduce_width += 1 ; 
    }

    size_t nBytesWritten = fprintf(pgmFile , "P%c\n%d %d\n%d\n",pgm->magic_number[1], reduce_width , reduce_height , pgm->maxGray);
    /* check if there is error */
    checkerror_return = check_bytesWritten(filename,nBytesWritten); 
    if (checkerror_return != 0)
        return checkerror_return; 

    /* check the magic number to see if it is binary or ASCII */
    /* for ascii */
    if(pgm->magic_number[1] == '2'){
         /* two for loop to print the value */
        for (int i = 0; i < pgm->height; i++){
            /* this value is to count when to make the new line */
            int count_reduce_print = 0;
            for (int j = 0; j < pgm->width; j++){
                /* if the value match the required print situation, print out. else print nothing */
                if( i % reduce_number == 0 && j % reduce_number == 0){
                    count_reduce_print++;
                    int nextCol = (count_reduce_print / reduce_width -1);
                    /* use uBytesWritten to check if there is error */
                    nBytesWritten =  fprintf(pgmFile, "%d%c", pgm->imageData[i][j], (nextCol ? ' ' : '\n'));
                    checkerror_return = check_bytesWritten(filename, nBytesWritten); 
                    /* if there is error, return it . else keep looping */
                    if (checkerror_return != 0)
                        return checkerror_return; 

                }
            }
        }
    }
    /* for binary */
    else if(pgm->magic_number[1] == '5'){
         /* two for loop to print the value */
        for (int i = 0; i < pgm->height; i++){
            for (int j = 0; j < pgm->width; j++){
                 /* if the value match the required print situation, print out. else print nothing */
                if(i % reduce_number == 0 && j% reduce_number == 0){
                    /* use uBytesWritten to check if there is error */
                    nBytesWritten = fwrite(&pgm->imageData[i][j], sizeof(unsigned char) , 1 ,pgmFile);
                    checkerror_return = check_bytesWritten(filename, nBytesWritten);
                    /* check if there is error */
                    if (checkerror_return != 0)
                        return checkerror_return;  
                }  
            }
        }
    }
    fclose(pgmFile); 
    return checkerror_return; 
}