/* library for I/O routines        */
#include <stdio.h>

/* library for memory routines     */
#include <stdlib.h>

#include "pgmStructure.h"
#include "pgmError.h"
#include "pgmReadAndWrite.h"
#include "pgmConvert.h"

/* convert ASCII to binary */
int pgma2b(PGMImage *pgm, const char *filename){
	/*read file */
    int return_read_file = readfile(pgm, filename);
	/*if magic number is not P2 return magic number error */
    if(return_read_file == 0){
        if(pgm->magic_number[1] == '5'){
            /*print error if wrong*/
            printf("ERROR: Bad Magic Number (%s)", filename);
            return EXIT_BAD_MAGIC_NUMBER;
        }
        /*convert if correct*/
        pgm->magic_number[1] = '5'; 
    }
	/*if read file has no error then write file*/
    return return_read_file; 
}

/* convert binary to ASCII*/
int pgmb2a(PGMImage *pgm, const char *filename){
    /*read file */
    /*if magic number is not P5 return magic number error */
    int return_read_file = readfile(pgm, filename);
    if(return_read_file == 0){
        if(pgm->magic_number[1] == '2'){
            /*print error if wrong*/
            printf("ERROR: Bad Magic Number (%s)", filename);
            return EXIT_BAD_MAGIC_NUMBER;
        }
        /*convert if correct*/
        pgm->magic_number[1] = '2'; 
    }
	/*if read file has no error then write file*/
    return return_read_file; 
}
