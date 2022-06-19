/* library for I/O routines        */
#include <stdio.h>

/* library for memory routines     */
#include <stdlib.h>

#include <string.h>

#include "pgmStructure.h"

#include "pgmError.h"
/***********************************/
/* check error function            */
/* return value that failed        */
/* return 0 if success             */
/***********************************/

int check_file(FILE *pgmFile, const char *filename){
    if (pgmFile == NULL){
        /*print error message and return */
        printf("ERROR: Bad File Name (%s)", filename);
        return EXIT_BAD_FILE_NAME; 
    }
    return EXIT_NO_ERRORS;
}
int check_outputfile(FILE *pgmFile, PGMImage *pgm, const char *filename){
    if(pgmFile == NULL){ 
        /* NULL output file */
		/* free memory                   */
		free(pgm->commentLine);
		free(pgm->imageData);
		/* print an error message        */
		printf("ERROR: Output Failed (%s)", filename);
		/* return an error code          */
		return OUTPUT_FAILED;
	} /* NULL output file */
    return EXIT_NO_ERRORS;
}
int check_magic_number(PGMImage *pgm,const char *filename, unsigned short *magic_Number, unsigned char magic_number){
    /*check if magic_number is in P2 or P5*/
    if(magic_number == '2'){
        if (*magic_Number != MAGIC_NUMBER_ASCII_PGM){
            /*free the magic number if not NULL*/
            if(pgm->magic_Number != NULL){
                free(pgm->magic_Number); 
            }
        /*print error message and return */
        printf("ERROR: Bad Magic Number (%s)", filename);
        return EXIT_BAD_MAGIC_NUMBER;
        }
    }
    else if (magic_number == '5'){
        if (*magic_Number != MAGIC_NUMBER_RAW_PGM){
            /*free the magic number if not NULL*/
            if(pgm->magic_Number != NULL){
                free(pgm->magic_Number); 
            }
        /*print error message and return */
        printf("ERROR: Bad Magic Number (%s)", filename);
        return EXIT_BAD_MAGIC_NUMBER;
        }
    }
    else{
        printf("ERROR: Bad Magic Number (%s)", filename);
        return EXIT_BAD_MAGIC_NUMBER;
    }
    return EXIT_NO_ERRORS;
}

int check_commentString(PGMImage *pgm, const char *filename, char *commentString){
    /* check for a comment line              */
    /* NULL means failure    */
    if(commentString == NULL || strlen(commentString) > MAX_COMMENT_LINE_LENGTH){ 
        /* free commendLine if not NULL */
        free(pgm->commentLine); 
        /*print error message and return */
        printf("ERROR: Bad Comment Line (%s)", filename);
        return BAD_COMMENT_LINE ; 
    } 
    return EXIT_NO_ERRORS;
}
int check_scanCount(const char *filename, int scanCount, int width, int height, int maxGray){
    /* sanity checks on size & grays         */
	/* must read exactly three values        */
    if(scanCount != 3){
        /*print error message and return */
        printf("ERROR: Bad Data (%s)", filename);
        return BAD_DATA; 
    }
    else if(
        /* checks on size */
            (width < MIN_IMAGE_DIMENSION	) 	||
		    (width >= MAX_IMAGE_DIMENSION	) 	||
		    (height < MIN_IMAGE_DIMENSION	) 	||
		    (height >= MAX_IMAGE_DIMENSION	)
            ){
                /*print error message and return */
                printf("ERROR: Bad Dimensions (%s)", filename);
                return BAD_DIMENSION;
    }
    else if (maxGray != 255){
        /* checks on Maxgrays*/
        /*print error message and return */
        printf("ERROR: Bad Max Gray Value (%s)", filename);
        return BAD_MAX_GRAY_VALUE; 
    }
    return EXIT_NO_ERRORS;
}


int check_imageData(const char *filename, unsigned char *imageData){
    /* sanity check for memory allocation    */
    if (imageData == NULL){
        /*print error message and return */
        printf("ERROR: Image Malloc Failed (%s)", filename);
        return IMAGE_MALLOC_FAILED; 
    }
    return EXIT_NO_ERRORS;
}

int check_grayValue(const char *filename, int grayValue, int scanCount){
    /* sanity check	                 */
    if ((scanCount != 1) || (grayValue < 0) || (grayValue > 255)){ 
        /* if fscanf failed */
        /*print error message and return */
        printf("ERROR: Bad Data (%s)", filename);
        return BAD_DATA;
    }
    return EXIT_NO_ERRORS; 
}
int check_bytesWritten(const char *filename ,size_t nBytesWritten){
    /* check that dimensions wrote correctly */
    if (nBytesWritten < 1){
        /* if dimensional write failed    */
        /*print error message and return */
        printf("ERROR: Output Failed (%s)", filename);
        return OUTPUT_FAILED; 
    }
    return EXIT_NO_ERRORS; 
}
int check_reducing_number(const char *filename, int width, int height, int reducing_num){
    if(width < reducing_num || height < reducing_num){
        return 100;
    }
    return EXIT_NO_ERRORS; 
}