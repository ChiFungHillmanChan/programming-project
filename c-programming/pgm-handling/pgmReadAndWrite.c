/* library for I/O routines        */
#include <stdio.h>

/* library for memory routines     */
#include <stdlib.h>

#include "pgmStructure.h"

#include "pgmError.h"

#include "pgmReadAndWrite.h"
/***********************************/
/* readfile function               */
/*This function is to read the file*/
/* returns 0 on success            */
/* non-zero error code on fail     */
/***********************************/
void structure(PGMImage *pgm){

    pgm->magic_number[0] = '0'; 
    pgm->magic_number[1] = '0';
    
    pgm->magic_Number = (unsigned short *) pgm->magic_number;        
	/* we will store ONE comment	         */
    
    pgm->commentLine = NULL;
	/* the logical width & height	         */
	/* note: cannot be negative	         */
    pgm->width= 0;
    pgm->height= 0;
    pgm->maxGray= 255;
	/* pointer to raw image data*/
	pgm->imageData = NULL; 
	/* allocate the data pointer             */
}
int readfile(PGMImage *pgm, const char *filename){
    /* this variable is to check the function returns value*/
    int checkerror_return = 0; 
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
    scanCount = fscanf(pgmFile, " %u %u %u", &(pgm->width), &(pgm->height), &(pgm->maxGray));

    checkerror_return = check_scanCount(filename, scanCount, pgm->width, pgm->height, pgm->maxGray);
    if (checkerror_return != 0)
        return checkerror_return;

    /* allocate the data pointer */    
    pgm->imageData = (unsigned char **)malloc(pgm->height * sizeof(*pgm->imageData));

    for (int i = 0; i < pgm->height; i++){
        pgm->imageData[i] = (unsigned char *) malloc(pgm->width * sizeof(unsigned char));
        checkerror_return = check_imageData(filename, pgm->imageData[i]);
        if (checkerror_return != 0)
            return checkerror_return;  
    }
    /*check error*/ 
    
    /* this variable is to check if there is extre data */ 
    int checktooMuchData = -1;
    /* pointer for efficient read ASCII code */
    if(pgm->magic_number[1] == '2'){
        for (int i = 0; i < pgm->height; i++){
            for (int j = 0; j < pgm->width; j++){
                int grayValue = -1;
                int scanCount =  fscanf(pgmFile, "%u", &grayValue);
                checkerror_return = check_grayValue(filename, grayValue, scanCount);
                if (checkerror_return != 0)
                    return checkerror_return; 
                pgm->imageData[i][j] = (unsigned char) grayValue;
            }
        }
        int scanCount = fscanf(pgmFile, "%u", &checktooMuchData);
        if(scanCount > 0){
            printf("ERROR: Bad Data (%s)", filename);
            return BAD_DATA;
        }
    }
    else if (pgm->magic_number[1] == '5'){
        fgetc(pgmFile); 
        //this will read the empty line
        /*read as binary*/
        for (int i = 0; i < pgm->height; i++){
            for(int j = 0; j < pgm->width; j++){
                int scanCount = fread(&pgm->imageData[i][j], sizeof(unsigned char),1, pgmFile);
                if(scanCount != 1){
                printf("ERROR: Bad Data (%s)", filename);
                    return BAD_DATA;
                }
            }
        }
        int scanCount = fscanf(pgmFile, "%u", &checktooMuchData);
        if(scanCount > 0){
            printf("ERROR: Bad Data (%s)", filename);
            return BAD_DATA;
        }
    }  
    // /*close file and return 0 as no error */
    fclose(pgmFile);
	return checkerror_return; 
}
/***********************************/
/* writefile function              */
/* This function is to write file  */
/* returns 0 on success            */
/* non-zero error code on fail     */
/***********************************/
int writefile(PGMImage *pgm,  const char *filename){
	/* open a file for writing               */
    /* this variable is to check the function returns value*/
    int checkerror_return = 0; 
    FILE *pgmFile = fopen(filename, "w");
    checkerror_return = check_outputfile(pgmFile, pgm, filename); 
    if (checkerror_return != 0)
        return checkerror_return; 
    
    /* write magic number, size & gray value */
    size_t nBytesWritten = fprintf(pgmFile , "P%c\n%d %d\n%d\n",pgm->magic_number[1], pgm->width , pgm->height, pgm->maxGray);
    /* check if there is error */
    checkerror_return = check_bytesWritten(filename,nBytesWritten); 
    if (checkerror_return != 0)
        return checkerror_return; 
    if(pgm->magic_number[1] == '2'){
        for (int i = 0; i < pgm->height; i++){
            for (int j = 0; j < pgm->width; j++){
                int nextCol = ( (j + 1) % pgm->width) ;
                nBytesWritten =  fprintf(pgmFile, "%d%c", pgm->imageData[i][j], (nextCol ? ' ' : '\n'));
                checkerror_return = check_bytesWritten(filename, nBytesWritten); 
                if (checkerror_return != 0)
                    return checkerror_return; 
            }
        }
    }
    else if(pgm->magic_number[1] == '5'){
        for (int i = 0; i < pgm->height; i++){
            for (int j = 0; j < pgm->width; j++){
                nBytesWritten = fwrite(&pgm->imageData[i][j], sizeof(unsigned char) , 1 ,pgmFile);
                checkerror_return = check_bytesWritten(filename, nBytesWritten);
                /* check if there is error */
                if (checkerror_return != 0)
                    return checkerror_return;    
            }
        }
    }
    fclose(pgmFile);
    return checkerror_return; 
}
