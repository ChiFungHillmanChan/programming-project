int check_file(FILE *pgmFile, const char *filename);
int check_outputfile(FILE *pgmFile, PGMImage *pgm, const char *filename); 
int check_magic_number(PGMImage *pgm, const char *filename, unsigned short *magic_Number, unsigned char magic_number);
int check_commentString(PGMImage *pgm, const char *filename, char *commentString);
int check_scanCount(const char *filename, int scanCount, int width, int height, int maxGray);
int check_imageData(const char *filename, unsigned char *imageData);
int check_grayValue(const char *filename, int grayValue, int scanCount);
int check_bytesWritten(const char *filename ,size_t nBytesWritten);
int check_reducing_number(const char *filename, int width, int height, int reducing_num);
