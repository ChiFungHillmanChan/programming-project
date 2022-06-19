/* library for I/O routines        */
#include <stdio.h>

/* library for memory routines     */
#include <stdlib.h>

#include <string.h>

#include <unistd.h>

#include "pgmStructure.h"

#include "pgmError.h"

#include "pgmReadAndWrite.h"

#include "pgmTile.h"

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
   
    int tile_number = 0;
	/* main() */
	/* check for correct number of arguments */
	if (argc == 1){
		/* check if argument is 0 */
		/* return special message indicating the correct usage and return 0 */
		printf("Usage: %s inputImage.pgm tiling_factor outputImage_<row>_<column>.pgm", argv[0]); 
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
    /* use this to split the output file */
    /* check the format of output file */
    /* if format wrong return error */
    /* check if the second argument line is number or not */
    tile_number = atoi(argv[2]); 
    /* if second argument is not a possitibe integer, return error */
    if( !tile_number || tile_number < 1){
        printf("ERROR: Miscellaneous (The division factor must be a positive integer)");
        return MISCELLANEOUS;
    }

    if( strstr(argv[3], "<row>") == NULL || strstr(argv[3], "<column>") == NULL ){
        /* print an error message        */
        printf("ERROR: Miscellaneous (Bad Template)");
        /* return an error code          */
        return MISCELLANEOUS;
    }
    if( strstr(argv[3], "_<row>_<column>.pgm") == NULL){
        /* print an error message        */
        printf("ERROR: Output Failed (%s)", argv[3]);
        /* return an error code          */
        return OUTPUT_FAILED;
    } 
    /* read file if success every checking */
    
    /*memory allocated structure*/
    PGMImage *pgm = malloc(sizeof(PGMImage)); 
	structure(pgm); 

    /* Use this function to read the file */
    int return_read_file = readfile(pgm, argv[1]);
    /* return error if exist, else continue */
    if(return_read_file != EXIT_NO_ERRORS)
        return return_read_file;

    /* this vairable is to store the string before "_<row>_<column>.pgm" */
    char buffer_takevalue[255];
    /* use a for loop to copy the string */
    for (int i = 0; i < strlen(argv[3]); i++){
        /* copy the string */
        buffer_takevalue[i] = argv[3][i];
        /* if the next string is '_<' , break the loop */
        if(argv[3][i+1] == '_' && argv[3][i+2] == '<'){
            break;
        }
    }
    /* this variable is for sprintf for tiling the file */
    char buffer_print[255];
    /* use two for loops to print and tile */
    for (int i = 0; i < tile_number; i++){
        for (int j = 0; j < tile_number; j++){
            /* use sprintf to print the output file name*/
            sprintf(buffer_print, "%s_%d_%d.pgm", buffer_takevalue, i, j);
            /* Go to tile file if no error in reading file */
            int return_tile_file = TileFile(pgm, buffer_print, i, j, tile_number);
            /* return error if have errors when tiling */
            if(return_tile_file != EXIT_NO_ERRORS){
                free(pgm); 
                return return_tile_file;
            }
        }
    }
    /*return value in tile file*/
    /* success tiling  */
    printf("TILED");
    /* free the pointer and return */
    free(pgm); 
    return EXIT_NO_ERRORS;  
}

int TileFile(PGMImage *pgm, const char *filename, int tile_i, int tile_j, int tile_number) {
	/* open a file for reducing file             */
    /* this variable is to check the function returns value*/
    int checkerror_return = 0; 
    /* open file for writing */
    FILE *pgmFile = fopen(filename, "w");

    checkerror_return = check_outputfile(pgmFile, pgm, filename); 
    /* check if the file is writeable */
    if (checkerror_return != 0)
        return checkerror_return;
    /* print initial data */
    size_t nBytesWritten = fprintf(pgmFile , "%c%c\n%d %d\n%d\n",pgm->magic_number[0], pgm->magic_number[1], pgm->width/tile_number ,pgm->height/tile_number,  pgm->maxGray);
    /* check if there is error */
    checkerror_return = check_bytesWritten(filename, nBytesWritten); 
    if (checkerror_return != 0)
        return checkerror_return; 

    /* check the magic number to see if it is binary or ASCII */
    /* for ascii */
    if(pgm->magic_number[1] == '2'){
         /* two for loops to print the value */
        for (int i = pgm->height/tile_number * tile_i ; i < pgm->height/tile_number * (tile_i + 1) ; i++){
            for (int j = pgm->width/tile_number * tile_j; j < pgm->width/tile_number * (tile_j + 1) ; j++){
                /* if the value matches the required print situation inside if else , print out. else print nothing */
                /* count when to print next column */
                int nextCol = ( (pgm->width / tile_number * ( tile_j + 1 ) - j - 1) );
                /* if it is the last line, print with different format (with space or only charactor */
                if(i == (pgm->height/tile_number * (tile_i + 1) - 1) && j == (pgm->width/tile_number * (tile_j + 1) -1 ) )
                    /* dont print next line if the file is going to end */
                    nBytesWritten =  fprintf(pgmFile, "%d", pgm->imageData[i][j]);
                else 
                    /* use uBytesWritten to check if there is error */
                    nBytesWritten =  fprintf(pgmFile, "%d%c", pgm->imageData[i][j], (nextCol ? ' ' : '\n'));
                /* check error for BytesWritten */   
                checkerror_return = check_bytesWritten(filename, nBytesWritten); 
                /* if there is error, return it . else keep looping */
                if (checkerror_return != 0)
                    return checkerror_return; 
            }
        }
    }
    /* for binary */
    else if(pgm->magic_number[1] == '5'){
        /* two for loops to print the value */
        for (int i = pgm->height/tile_number * tile_i ; i < pgm->height/tile_number * (tile_i + 1); i++){
            for (int j = pgm->width/tile_number * tile_j; j < pgm->width/tile_number * (tile_j + 1); j++){
                /* if the value matches the required print situation inside if else , print out. else print nothing */
                /* use uBytesWritten to check if there is error */
                nBytesWritten = fwrite(&pgm->imageData[i][j], sizeof(unsigned char) , 1 ,pgmFile);
                checkerror_return = check_bytesWritten(filename, nBytesWritten);
                /* check if there is error */
                if (checkerror_return != 0)
                    return checkerror_return;  
            }
        }
    }
    /* successful tiling!! Close the file and return everything */
    fclose(pgmFile); 
    return checkerror_return; 
}