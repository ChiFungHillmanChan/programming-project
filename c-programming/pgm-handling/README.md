# C Programming Projects

BY CHI FUNG HILLMAN CHAN

## Directory: pgm-handling
pgm-handling folder contains: 
- ASCIIfile folder for ASCII pgmfile
- BinaryFile folder for binary pgmfile 
- Makefile
- modules.txt
- .c files x10
- header files x8 
- testplan.txt
- testscript.sh

## Run function 

1.  Go To the pgm-handling directory to run the file.

2.  Use 'Make' command to start running the files.
```bash
make
```

3.  There are 7 main files to execite:
- 3.1.    pgmEcho:
The programme "Echo" should take 2 arguments: input file name and output file name.
The file will read the input file data and store it. If there is no error after reading, the echo an exactly same file data and write it as the output file name.
```bash
./pgmEcho inputImage.pgm outputImage.pgm
``` 
    
- 3.2.    pgmComp:
The programme "Comp" should take 2 arguments: two input files name. 
The file will read two input file data and store it. If there is no error, compare them and see if they are identical.
This programme accept both binary and ASCII.
```bash
./pgmComp inputImage.pgm inputImage.pgm
``` 
    
- 3.3.    pgma2b:
The programme "a2b" should take 2 arguments: input file with ASCII data and output file with Binary data.
The file will read the input file data and store it. If there is no error after reading, it will convert the ASCII data to binary and write it as the output file name.
```bash
./pgma2b inputImage.pgm outputImage.pgm
```    
- 3.4.    pgmb2a:
The programme "b2a" should take 2 arguments: input file with binary data and output file with ASCII data.
The file will read the input file data and store it. If there is no error after reading, it will convert the binary data to ASCII and write it as the output file name.
```bash
./pgma2b inputImage.pgm outputImage.pgm
```   
    
- 3.5.    pgmReduce:
The programme "Reduce" should take 3 arguments : input file name, reduce factor and output file name.
The file will read the input file data and store it. If there is no error after reading, it will reduce the input file data by reduce number and write it as the ouput file name.
```bash
./pgmReduce inputImage.pgm reduction_factor outputImage.pgm
```

- 3.6.    pgmTile:
The programme "Reduce" should take 3 arguments : input file name, tile factor and output file name with the required format "_<row>_<column>.pgm".
The file will read the input file data and store it. If there is no error after reading, it will tile the input file data by tile number.
Then split it to multiple files and replace the <row> and <column> to specific integer. 
```bash
./pgmTile inputImage.pgm tiling_factor "outputImage_<row>_<column>.pgm"
```

- 3.7     pgmAssemble:
The programme "Assemble" should take 3i + 1 arguments : output file name, output file's width, output file's height, and multiple number of : row, column, input files name.
The file will read the output file and see if it is writeable. If there is no error, it will store the width and height to the structure.
After that, the programme will read each of the data and store it to the specific row and column by reading the argument number.
Finally output the file if there is no error on every input file.
```bash
./pgmAssemble outputImage.pgm width height "(row column inputImage.pgm)+"
```
4.  Use the command "make clean" to delete all the files made by "make"
```bash
make clean
```

5.  There is a testscript.sh file for testing every possible error and check the output. 
    Use the suggested command "sh testscript.sh"
    It will automatically run all the function starting with "make" and end with "make clean"
    Then compare the expected output and actual output. 
    At the bottom of the testscript, it count the total test number and tha failing test also. 
    If the file is not exist , it wont show the related testing. 
```bash
sh testscript.sh
```


