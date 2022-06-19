#define EXIT_NO_ERRORS 0
#define EXIT_WRONG_ARG_COUNT 1
#define EXIT_BAD_FILE_NAME 2
#define EXIT_BAD_MAGIC_NUMBER 3
#define	BAD_COMMENT_LINE 4
#define BAD_DIMENSION 5
#define BAD_MAX_GRAY_VALUE 6
#define IMAGE_MALLOC_FAILED 7
#define BAD_DATA 8
#define OUTPUT_FAILED 9
#define BAD_LAYOUT 10
#define MISCELLANEOUS 100


#define MAGIC_NUMBER_RAW_PGM 0x3550
#define MAGIC_NUMBER_ASCII_PGM 0x3250
#define MIN_IMAGE_DIMENSION 1
#define MAX_IMAGE_DIMENSION 65536
#define MAX_COMMENT_LINE_LENGTH 128
/***********************************/
/* Type structure                  */
/***********************************/
typedef struct PGMImage {
	/* the magic number		         */
	/* stored as two bytes to avoid	         */
	/* problems with endianness	         */
	/* Raw:    0x5035 or P5		         */
	/* ASCII:  0x5032 or P2		*/
	unsigned char magic_number[2];
	unsigned short *magic_Number;      
	/* we will store ONE comment	         */
    char *commentLine; 
	/* the logical width & height	         */
	/* note: cannot be negative	         */
    unsigned int width;
    unsigned int height;
    unsigned int maxGray;
	/* pointer to raw image data*/
	unsigned char **imageData; 

} PGMImage;
