/* library for I/O routines        */
#include <stdio.h>

/* library for memory routines     */
#include <stdlib.h>

/*include other header file for function*/
#include "pgmStructure.h"
#include "pgmReadAndWrite.h"
#include "pgmError.h"
#include "pgmConvert.h"
#include "pgmComp.h"

int main(int argc, char **argv){
    /* main() */
	/* check for correct number of arguments */

    /*memory allocated pgm structure*/
    PGMImage *pgm_file1 = malloc(sizeof(PGMImage)); 
    PGMImage *pgm_file2 = malloc(sizeof(PGMImage));
    structure(pgm_file1);
    structure(pgm_file2);  

    if(argc == 1){
        /* check if argument is 0*/
		/* return special message indicating the correct usage and return 0*/
        printf("Usage: %s inputImage.pgm inputImage.pgm", argv[0]);
        return EXIT_NO_ERRORS; 
    }
    else if(argc != 3){
        /* print an error message        */
		printf("ERROR: Bad Argument Count");
		/* and return an error code      */
		return EXIT_WRONG_ARG_COUNT;
    }
    /*go to read file function to check if they have any error for file 1*/
    int readpgmfile1 = readfile(pgm_file1 ,argv[1]);
    if(readpgmfile1 != 0){
        return readpgmfile1; 
    }
    /*go to read file function to check if they have any error for file 2*/
    int readpgmfile2 = readfile(pgm_file2, argv[2]); 
    if(readpgmfile2 != 0){
        return readpgmfile2; 
    }

    /* Go to compare file function to check if they are identical*/
    compare_two_file(pgm_file1, pgm_file2, argv[1]); 
    /*return 0 after successful compare*/
    return EXIT_NO_ERRORS;
}

/* programming for comparing two files after successful checking */
int compare_two_file(PGMImage *pgm1, PGMImage *pgm2, const char *filename){
    int checkerror = EXIT_NO_ERRORS; 
    
    if(pgm1->magic_number[1] != pgm2->magic_number[1] && pgm1->magic_number[1] == '2'){
        /* if their file format is different with file1 is ASCII, change to binary*/
        checkerror = pgma2b(pgm1, filename); 
        if(checkerror != 0)
            return checkerror; 
    }
    else if (pgm1->magic_number[1] != pgm2->magic_number[1] && pgm1->magic_number[1] == '5'){
        /* if their file format is different with file1 is binary, change to ASCII*/
        checkerror = pgmb2a(pgm1, filename); 
        if(checkerror != 0)
            return checkerror; 
    }
    goto checkidentical; 

    /* check identical */
    checkidentical:
        /*compare imageData*/
        for (int i = 0; i < pgm1->height; i++){ 
            for (int j = 0; j < pgm1->width; j++){
                if(pgm1->imageData[i][j] != pgm2->imageData[i][j]){
                printf("DIFFERENT");
                return EXIT_NO_ERRORS;
                } 
            } 
        }
        /*compare other everything for the pgm file*/
        /*command line, width, height and maxgray to see if they are logically identical*/
        if((pgm1->commentLine != pgm2->commentLine) ||
            (pgm1->width != pgm2->width) || 
            (pgm1->height != pgm2->height) || 
            (pgm1->maxGray != pgm2->maxGray))
            {
            /* check if file is not identical*/
            printf("DIFFERENT");
            
            return EXIT_NO_ERRORS; 
        }   
        else{
            /*else identical */
            printf("IDENTICAL");
            return EXIT_NO_ERRORS;
        }
}
