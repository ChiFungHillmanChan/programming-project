#!/bin/bash
make

echo "\nStart Testing\n"

counter=0

counttest=0

FILE=pgmEcho.c
if test -f "$FILE";
then echo "\npgmEcho file exist"
    echo "                                                                                                                                      PASSED"

    echo "pgmEcho No Argument"
    if  ./pgmEcho | grep -q 'Usage: ./pgmEcho inputImage.pgm outputImage.pgm' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: Usage: ./pgmEcho inputImage.pgm outputImage.pgm"
    echo "ACTUAL  : \c" 
    ./pgmEcho


    echo "\n\npgmEcho Wrong Argument Line"
    if  ./pgmEcho WrongArgument | grep -q 'ERROR: Bad Argument Count' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Argument Count"
    echo "ACTUAL  : \c" 
    ./pgmEcho WrongArgument


    echo "\n\npgmEcho Bad file Name"
    if  ./pgmEcho wrongFileName output.pgm | grep -q 'ERROR: Bad File Name' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad File Name (wrongFileName)"
    echo "ACTUAL  : \c" 
    ./pgmEcho wrongFileName output.pgm




    echo "\n\npgmEcho Bad Comment Line"
    if  ./pgmEcho ./ASCIIfile/badCommentLine.pgm output.pgm | grep -q 'ERROR: Bad Comment Line' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Comment Line (./ASCIIfile/badCommentLine.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./ASCIIfile/badCommentLine.pgm output.pgm



    echo "\n\npgmEcho Bad Magic Number"
    if  ./pgmEcho ./ASCIIfile/badMagicNumber.pgm output.pgm | grep -q 'ERROR: Bad Magic Number' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Magic Number (./ASCIIfile/badMagicNumber.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./ASCIIfile/badMagicNumber.pgm output.pgm



    echo "\n\npgmEcho Bad Dimension < 1"
    if  ./pgmEcho ./ASCIIfile/badWidthDimension.pgm output.pgm | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./ASCIIfile/badWidthDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./ASCIIfile/badWidthDimension.pgm output.pgm



    echo "\n\npgmEcho Bad Dimension > 65536"
    if  ./pgmEcho ./ASCIIfile/badHeightDimension.pgm output.pgm | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./ASCIIfile/badHeightDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./ASCIIfile/badHeightDimension.pgm output.pgm



    echo "\n\npgmEcho Bad Max Gray Value"
    if  ./pgmEcho ./ASCIIfile/badMaxGray.pgm output.pgm | grep -q 'ERROR: Bad Max Gray Value' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Max Gray Value (./ASCIIfile/badMaxGray.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./ASCIIfile/badMaxGray.pgm output.pgm



    echo "\n\npgmEcho Too Little Data"
    if  ./pgmEcho ./ASCIIfile/TooLittleData.pgm output.pgm | grep -q 'ERROR: Bad Data' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Data (./ASCIIfile/TooLittleData.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./ASCIIfile/TooLittleData.pgm output.pgm



    echo "\n\npgmEcho Too Much Data"
    if  ./pgmEcho ./ASCIIfile/TooMuchData.pgm output.pgm | grep -q 'ERROR: Bad Data' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Data (./ASCIIfile/TooMuchData.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./ASCIIfile/TooMuchData.pgm output.pgm



    echo "\n\npgmEcho Wrong Output File"
    if  ./pgmEcho ./ASCIIfile/slice0a.pgm  ./WrongFilePath/output.pgm | grep -q 'ERROR: Output Failed' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Output Failed (./WrongFilePath/output.pgm)"
    echo "ACTUAL  : \c"
    ./pgmEcho ./ASCIIfile/slice0a.pgm  ./WrongFilePath/output.pgm



    echo "\n\npgmEcho Correct Return for ASCII"
    if  ./pgmEcho ./ASCIIfile/slice0a.pgm ./ASCIIfile/output.pgm | grep -q 'ECHOED' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ECHOED"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./ASCIIfile/slice0a.pgm ./ASCIIfile/output.pgm



    echo "\n\npgmEcho Bad Magic Number"
    if  ./pgmEcho ./BinaryFile/badMagicNumber.pgm output.pgm | grep -q 'ERROR: Bad Magic Number' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Magic Number (./BinaryFile/badMagicNumber.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./BinaryFile/badMagicNumber.pgm output.pgm



    echo "\n\npgmEcho Bad Dimension < 1"
    if  ./pgmEcho ./BinaryFile/badwidthDimension.pgm output. | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./BinaryFile/badWidthDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./BinaryFile/badwidthDimension.pgm output.



    echo "\n\npgmEcho Bad Dimension > 65536"
    if  ./pgmEcho ./BinaryFile/badHeightDimension.pgm output.pgm | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./BinaryFile/badHeightDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./BinaryFile/badHeightDimension.pgm output.pgm



    echo "\n\npgmEcho Bad Max Gray Value"
    if  ./pgmEcho ./BinaryFile/badMaxGray.pgm output.pgm | grep -q 'ERROR: Bad Max Gray Value' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Max Gray Value (./BinaryFile/badMaxGray.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./BinaryFile/badMaxGray.pgm output.pgm



    echo "\n\npgmEcho Too Little Data"
    if  ./pgmEcho ./BinaryFile/TooLittleData.pgm output.pgm | grep -q 'ERROR: Bad Data' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Data (./BinaryFile/TooLittleData.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./BinaryFile/TooLittleData.pgm output.pgm



    echo "\n\npgmEcho Correct Return for Binary"
    if  ./pgmEcho ./BinaryFile/baboon.pgm ./BinaryFile/output.pgm | grep -q 'ECHOED' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ECHOED"
    echo "ACTUAL  : \c" 
    ./pgmEcho ./BinaryFile/baboon.pgm ./BinaryFile/output.pgm

    echo "\n"
else
    echo "\npgmEcho file does not exist"
    echo "                                                                                                                                      FAILED"
    : $((counter++)); 
fi

echo "______________________________________________________________________________________________________________________________________________\n"


FILE=pgmComp.c
if test -f "$FILE";
then echo "\npgmComp file exist"
    echo "                                                                                                                                      PASSED"
    echo "pgmComp No Argument"
    if  ./pgmComp | grep -q 'Usage: ./pgmComp inputImage.pgm inputImage.pgm' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: Usage: ./pgmComp inputImage.pgm inputImage.pgm"
    echo "ACTUAL  : \c" 
    ./pgmComp



    echo "\n\npgmComp Wrong Argument Line"
    if  ./pgmComp WrongArgument | grep -q 'ERROR: Bad Argument Count' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Argument Count"
    echo "ACTUAL  : \c" 
    ./pgmComp WrongArgument



    echo "\n\npgmComp Bad File Name"
    if  ./pgmComp wrongFileName output.pgm | grep -q 'ERROR: Bad File Name' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad File Name (wrongFileName)"
    echo "ACTUAL  : \c" 
    ./pgmComp wrongFileName output.pgm



    echo "\n\npgmComp Bad Comment Line"
    if  ./pgmComp ./ASCIIfile/badCommentLine.pgm output.pgm | grep -q 'ERROR: Bad Comment Line' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Comment Line (./ASCIIfile/badCommentLine.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmComp ./ASCIIfile/badCommentLine.pgm output.pgm



    echo "\n\npgmComp Bad Magic Number"
    if  ./pgmComp ./ASCIIfile/badMagicNumber.pgm output.pgm | grep -q 'ERROR: Bad Magic Number' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Magic Number (./ASCIIfile/badMagicNumber.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmComp ./ASCIIfile/badMagicNumber.pgm output.pgm



    echo "\n\npgmComp Bad Dimension < 1"
    if  ./pgmComp ./ASCIIfile/badWidthDimension.pgm output.pgm | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./ASCIIfile/badWidthDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmComp ./ASCIIfile/badWidthDimension.pgm output.pgm



    echo "\n\npgmComp Bad Dimension > 65536"
    if  ./pgmComp ./ASCIIfile/badHeightDimension.pgm output.pgm | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./ASCIIfile/badHeightDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmComp ./ASCIIfile/badHeightDimension.pgm output.pgm



    echo "\n\npgmComp Bad Max Gray Value"
    if  ./pgmComp ./ASCIIfile/badMaxGray.pgm output.pgm | grep -q 'ERROR: Bad Max Gray Value' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Max Gray Value (./ASCIIfile/badMaxGray.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmComp ./ASCIIfile/badMaxGray.pgm output.pgm



    echo "\n\npgmComp Too Little Data"
    if  ./pgmComp ./ASCIIfile/TooLittleData.pgm output.pgm | grep -q 'ERROR: Bad Data' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Data (./ASCIIfile/TooLittleData.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmComp ./ASCIIfile/TooLittleData.pgm output.pgm



    echo "\n\npgmComp Too Much Data"
    if  ./pgmComp ./ASCIIfile/TooMuchData.pgm output.pgm | grep -q 'ERROR: Bad Data' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Data (./ASCIIfile/TooMuchData.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmComp ./ASCIIfile/TooMuchData.pgm output.pgm



    echo "\n\npgmComp Correct Return ASCII Compare ASCII Identical"
    if  ./pgmComp ./ASCIIfile/slice0a.pgm ./ASCIIfile/output.pgm | grep -q 'IDENTICAL' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: IDENTICAL"
    echo "ACTUAL  : \c" 
    ./pgmComp ./ASCIIfile/slice0a.pgm ./ASCIIfile/output.pgm



    echo "\n\npgmComp Correct Return ASCII compare ASCII Non-Identical"
    if  ./pgmComp ./ASCIIfile/slice0a.pgm ./ASCIIfile/baboon.pgm | grep -q 'DIFFERENT' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: DIFFERENT"
    echo "ACTUAL  : \c" 
    ./pgmComp ./ASCIIfile/slice0a.pgm ./ASCIIfile/baboon.pgm



    echo "\n\npgmComp Bad Magic Number"
    if  ./pgmComp ./BinaryFile/badMagicNumber.pgm output.pgm | grep -q 'ERROR: Bad Magic Number' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Magic Number (./BinaryFile/badMagicNumber.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmComp ./BinaryFile/badMagicNumber.pgm output.pgm



    echo "\n\npgmComp Bad Dimension < 1"
    if  ./pgmComp ./BinaryFile/badwidthDimension.pgm output. | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./BinaryFile/badWidthDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmComp ./BinaryFile/badwidthDimension.pgm output.



    echo "\n\npgmComp Bad Dimension > 65536"
    if  ./pgmComp ./BinaryFile/badHeightDimension.pgm output.pgm | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./BinaryFile/badHeightDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmComp ./BinaryFile/badHeightDimension.pgm output.pgm



    echo "\n\npgmComp Bad Max Gray Value"
    if  ./pgmComp ./BinaryFile/badMaxGray.pgm output.pgm | grep -q 'ERROR: Bad Max Gray Value' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Max Gray Value (./BinaryFile/badMaxGray.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmComp ./BinaryFile/badMaxGray.pgm output.pgm



    echo "\n\npgmComp Too Little Data"
    if  ./pgmComp ./BinaryFile/TooLittleData.pgm output.pgm | grep -q 'ERROR: Bad Data' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Data (./BinaryFile/TooLittleData.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmComp ./BinaryFile/TooLittleData.pgm output.pgm



    echo "\n\npgmEcho Wrong Output File"
    if  ./pgmComp ./ASCIIfile/slice0a.pgm ./WrongFilePath/output.pgm | grep -q 'ERROR: Bad File Name' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad File Name (./WrongFilePath/output.pgm)"
    echo "ACTUAL  : \c"
    ./pgmComp ./ASCIIfile/slice0a.pgm ./WrongFilePath/output.pgm



    echo "\n\npgmComp Correct Return Binary Compare Binary Identical"
    if  ./pgmComp ./BinaryFile/baboon.pgm ./BinaryFile/output.pgm | grep -q 'IDENTICAL' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: IDENTICAL"
    echo "ACTUAL  : \c" 
    ./pgmComp ./BinaryFile/baboon.pgm ./BinaryFile/output.pgm



    echo "\n\npgmComp Correct Return Binary Compare Binary Non-Identical"
    if  ./pgmComp ./BinaryFile/baboon.pgm ./BinaryFile/slice0b.pgm | grep -q 'DIFFERENT' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: DIFFERENT"
    echo "ACTUAL  : \c" 
    ./pgmComp ./BinaryFile/baboon.pgm ./BinaryFile/slice0b.pgm



    echo "\n\npgmComp Correct Return ASCII Compare Binary Identical"
    if  ./pgmComp ./ASCIIfile/baboon.pgm ./BinaryFile/baboon.pgm | grep -q 'IDENTICAL' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: IDENTICAL"
    echo "ACTUAL  : \c" 
    ./pgmComp ./ASCIIfile/baboon.pgm ./BinaryFile/baboon.pgm



    echo "\n\npgmComp Correct Return Binary Compare ASCII Identical"
    if  ./pgmComp ./BinaryFile/slice0b.pgm ./ASCIIfile/slice0a.pgm | grep -q 'IDENTICAL' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: IDENTICAL"
    echo "ACTUAL  : \c" 
    ./pgmComp ./BinaryFile/slice0b.pgm ./ASCIIfile/slice0a.pgm

    echo "\n"
else
    echo "\npgmComp file does not exist"
    echo "                                                                                                                                      FAILED"
    : $((counter++)); 
fi

    echo "______________________________________________________________________________________________________________________________________________\n"


FILE=pgma2b.c
if test -f "$FILE";
then echo "\npgma2b file exist"
    echo "                                                                                                                                      PASSED"
    echo "pgma2b No Argument"
    if  ./pgma2b | grep -q 'Usage: ./pgma2b inputImage.pgm outputImage.pgm' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: Usage: ./pgma2b inputImage.pgm outputImage.pgm"
    echo "ACTUAL  : \c" 
    ./pgma2b



    echo "\n\npgma2b Wrong Argument Line"
    if  ./pgma2b WrongArgument | grep -q 'ERROR: Bad Argument Count' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Argument Count"
    echo "ACTUAL  : \c" 
    ./pgma2b WrongArgument



    echo "\n\npgma2b Bad file Name"
    if  ./pgma2b wrongFileName output.pgm | grep -q 'ERROR: Bad File Name' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad File Name (wrongFileName)"
    echo "ACTUAL  : \c" 
    ./pgma2b wrongFileName output.pgm



    echo "\n\npgma2b Bad Comment Line"
    if  ./pgma2b ./ASCIIfile/badCommentLine.pgm output.pgm | grep -q 'ERROR: Bad Comment Line' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Comment Line (./ASCIIfile/badCommentLine.pgm)"
    echo "ACTUAL  : \c" 
    ./pgma2b ./ASCIIfile/badCommentLine.pgm output.pgm



    echo "\n\npgma2b Bad Magic Number"
    if  ./pgma2b ./ASCIIfile/badMagicNumber.pgm output.pgm | grep -q 'ERROR: Bad Magic Number' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Magic Number (./ASCIIfile/badMagicNumber.pgm)"
    echo "ACTUAL  : \c" 
    ./pgma2b ./ASCIIfile/badMagicNumber.pgm output.pgm



    echo "\n\npgma2b Bad Dimension < 1"
    if  ./pgma2b ./ASCIIfile/badWidthDimension.pgm output.pgm | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./ASCIIfile/badWidthDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgma2b ./ASCIIfile/badWidthDimension.pgm output.pgm



    echo "\n\npgma2b Bad Dimension > 65536"
    if  ./pgma2b ./ASCIIfile/badHeightDimension.pgm output.pgm | grep -q 'ERROR: Bad Dimensions ' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./ASCIIfile/badHeightDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgma2b ./ASCIIfile/badHeightDimension.pgm output.pgm



    echo "\n\npgma2b Bad Max Gray Value"
    if  ./pgma2b ./ASCIIfile/badMaxGray.pgm output.pgm | grep -q 'ERROR: Bad Max Gray Value' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Max Gray Value (./ASCIIfile/badMaxGray.pgm)"
    echo "ACTUAL  : \c" 
    ./pgma2b ./ASCIIfile/badMaxGray.pgm output.pgm



    echo "\n\npgma2b Too Little Data"
    if  ./pgma2b ./ASCIIfile/TooLittleData.pgm output.pgm | grep -q 'ERROR: Bad Data' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Data (./ASCIIfile/TooLittleData.pgm)"
    echo "ACTUAL  : \c" 
    ./pgma2b ./ASCIIfile/TooLittleData.pgm output.pgm



    echo "\n\npgma2b Too Much Data"
    if  ./pgma2b ./ASCIIfile/TooMuchData.pgm output.pgm | grep -q 'ERROR: Bad Data' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Data (./ASCIIfile/TooMuchData.pgm)"
    echo "ACTUAL  : \c" 
    ./pgma2b ./ASCIIfile/TooMuchData.pgm output.pgm



    echo "\n\npgma2b Input Binary File"
    if  ./pgma2b ./BinaryFile/output.pgm output.pgm | grep -q 'ERROR: Bad Magic Number' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Magic Number (./BinaryFile/output.pgm)"
    echo "ACTUAL  : \c" 
    ./pgma2b ./BinaryFile/output.pgm output.pgm



    echo "\n\npgma2b Successfully Convert"
    if  ./pgma2b ./ASCIIfile/slice0a.pgm ./BinaryFile/convertedFromASCII.pgm | grep -q 'CONVERTED' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: CONVERTED"
    echo "ACTUAL  : \c" 
    ./pgma2b ./ASCIIfile/slice0a.pgm ./BinaryFile/convertedFromASCII.pgm

    echo "\n"
else
    echo "\npgma2b file does not exist"
    echo "                                                                                                                                      FAILED"
    : $((counter++)); 
fi
echo "______________________________________________________________________________________________________________________________________________\n"

FILE=pgmb2a.c
if test -f "$FILE";
then echo "\npgmb2a file exist"
    echo "                                                                                                                                      PASSED"
    echo "pgmb2a No Argument"
    if  ./pgmb2a | grep -q 'Usage: ./pgmb2a inputImage.pgm outputImage.pgm' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: Usage: ./pgmb2a inputImage.pgm outputImage.pgm"
    echo "ACTUAL  : \c" 
    ./pgmb2a



    echo "\n\npgmb2a Wrong Argument Line"
    if  ./pgmb2a WrongArgument | grep -q 'ERROR: Bad Argument Count' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Argument Count"
    echo "ACTUAL  : \c" 
    ./pgmb2a WrongArgument



    echo "\n\npgmb2a Bad file Name"
    if  ./pgmb2a wrongFileName output.pgm | grep -q 'ERROR: Bad File Name' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad File Name (wrongFileName)"
    echo "ACTUAL  : \c" 
    ./pgmb2a wrongFileName output.pgm



    echo "\n\npgmb2a Bad Magic Number"
    if  ./pgmb2a ./BinaryFile/badMagicNumber.pgm output.pgm | grep -q 'ERROR: Bad Magic Number' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Magic Number (./BinaryFile/badMagicNumber.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmb2a ./BinaryFile/badMagicNumber.pgm output.pgm



    echo "\n\npgmb2a Bad Dimension < 1"
    if  ./pgmb2a ./BinaryFile/badWidthDimension.pgm output.pgm | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./BinaryFile/badWidthDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmb2a ./BinaryFile/badWidthDimension.pgm output.pgm



    echo "\n\npgmb2a Bad Dimension > 65536"
    if  ./pgmb2a ./BinaryFile/badHeightDimension.pgm output.pgm | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./BinaryFile/badHeightDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmb2a ./BinaryFile/badHeightDimension.pgm output.pgm



    echo "\n\npgmb2a Bad Max Gray Value"
    if  ./pgmb2a ./BinaryFile/badMaxGray.pgm output.pgm | grep -q 'ERROR: Bad Max Gray Value' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Max Gray Value (./BinaryFile/badMaxGray.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmb2a ./BinaryFile/badMaxGray.pgm output.pgm



    echo "\n\npgmab2a Too Little Data"
    if  ./pgmb2a ./BinaryFile/TooLittleData.pgm output.pgm | grep -q 'ERROR: Bad Data' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Data (./BinaryFile/TooLittleData.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmb2a ./BinaryFile/TooLittleData.pgm output.pgm



    echo "\n\npgmb2a Input ASCII File"
    if  ./pgmb2a ./ASCIIfile/output.pgm output.pgm | grep -q 'ERROR: Bad Magic Number' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Magic Number (./ASCIIfile/output.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmb2a ./ASCIIfile/output.pgm output.pgm



    echo "\n\npgma2b Successfully Convert"
    if  ./pgmb2a ./BinaryFile/baboon.pgm ./ASCIIfile/baboon.pgm | grep -q 'CONVERTED' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: CONVERTED"
    echo "ACTUAL  : \c" 
    ./pgmb2a ./BinaryFile/baboon.pgm ./ASCIIfile/baboon.pgm

    echo "\n"
else
    echo "\npgmb2a file does not exist"
    echo "                                                                                                                                      FAILED"
    : $((counter++)); 
fi

echo "______________________________________________________________________________________________________________________________________________\n"


FILE=pgmReduce.c
if test -f "$FILE";
then echo "\npgmReduce file exist"
    echo "                                                                                                                                      PASSED"
    echo "pgmReduce No Argument"
    if  ./pgmReduce | grep -q 'Usage: ./pgmReduce inputImage.pgm reduction_factor outputImage.pgm' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: Usage: ./pgmReduce inputImage.pgm reduction_factor outputImage.pgm"
    echo "ACTUAL  : \c" 
    ./pgmReduce



    echo "\n\npgmReduce Wrong Argument Line"
    if  ./pgmReduce WrongArgument | grep -q 'ERROR: Bad Argument Count' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Argument Count"
    echo "ACTUAL  : \c" 
    ./pgmReduce WrongArgument



    echo "\n\npgmReduce Input Non-numeric Reduce Number"
    if  ./pgmReduce ./ASCIIfile/baboon.pgm NonNumeric output.pgm | grep -q 'ERROR: Miscellaneous' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Miscellaneous (The reduction factor must be a possitive integer"
    echo "ACTUAL  : \c" 
    ./pgmReduce ./ASCIIfile/baboon.pgm NonNumeric output.pgm



    echo "\n\npgmReduce Input negative Reduce Number"
    if  ./pgmReduce ./ASCIIfile/slice0a.pgm -1 output.pgm | grep -q 'ERROR: Miscellaneous' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Miscellaneous (The reduction factor must be a possitive integer)"
    echo "ACTUAL  : \c" 
    ./pgmReduce ./ASCIIfile/slice0a.pgm -1 output.pgm



    echo "\n\npgmReduce Bad file Name"
    if  ./pgmReduce wrongFileName 5 output.pgm | grep -q 'ERROR: Bad File Name' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad File Name (wrongFileName)"
    echo "ACTUAL  : \c" 
    ./pgmReduce wrongFileName 5 output.pgm



    echo "\n\npgmReduce Bad Comment Line"
    if  ./pgmReduce ./ASCIIfile/badCommentLine.pgm 5 output.pgm | grep -q 'ERROR: Bad Comment Line' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Comment Line (./ASCIIfile/badCommentLine.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmReduce ./ASCIIfile/badCommentLine.pgm 5 output.pgm



    echo "\n\npgmReduce Bad Magic Number"
    if  ./pgmReduce ./ASCIIfile/badMagicNumber.pgm 5 output.pgm | grep -q 'ERROR: Bad Magic Number' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Magic Number (./ASCIIfile/badMagicNumber.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmReduce ./ASCIIfile/badMagicNumber.pgm 5 output.pgm



    echo "\n\npgmReduce Bad Dimension < 1"
    if  ./pgmReduce ./ASCIIfile/badWidthDimension.pgm 5 output.pgm | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./ASCIIfile/badWidthDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmReduce ./ASCIIfile/badWidthDimension.pgm 5 output.pgm



    echo "\n\npgmReduce Bad Dimension > 65536"
    if  ./pgmReduce ./ASCIIfile/badHeightDimension.pgm 5 output.pgm | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./ASCIIfile/badHeightDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmReduce ./ASCIIfile/badHeightDimension.pgm 5 output.pgm



    echo "\n\npgmReduce Bad Max Gray Value"
    if  ./pgmReduce ./ASCIIfile/badMaxGray.pgm 5 output.pgm | grep -q 'ERROR: Bad Max Gray Value' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Max Gray Value (./ASCIIfile/badMaxGray.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmReduce ./ASCIIfile/badMaxGray.pgm 5 output.pgm



    echo "\n\npgmReduce Too Little Data"
    if  ./pgmReduce ./ASCIIfile/TooLittleData.pgm 5 output.pgm | grep -q 'ERROR: Bad Data' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Data (./ASCIIfile/TooLittleData.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmReduce ./ASCIIfile/TooLittleData.pgm 5 output.pgm



    echo "\n\npgmReduce Too Much Data"
    if  ./pgmReduce ./ASCIIfile/TooMuchData.pgm 5 output.pgm | grep -q 'ERROR: Bad Data' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Data (./ASCIIfile/TooMuchData.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmReduce ./ASCIIfile/TooMuchData.pgm 5 output.pgm



    echo "\n\npgmReduce Successfully Reduce File"
    if  ./pgmReduce ./ASCIIfile/baboon.pgm 5 ./BinaryFile/Reduced.pgm | grep -q 'REDUCED' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: REDUCED"
    echo "ACTUAL  : \c" 
    ./pgmReduce ./ASCIIfile/baboon.pgm 5 ./BinaryFile/Reduced.pgm

    echo "\n"
else
    echo "\npgmReduce file does not exist"
    echo "                                                                                                                                      FAILED"
    : $((counter++)); 
fi


echo "______________________________________________________________________________________________________________________________________________\n"


FILE=pgmTile.c
if test -f "$FILE";
then echo "\npgmTile file exist"

    echo "                                                                                                                                      PASSED"
    echo "pgmTile No Argument"
    if  ./pgmTile | grep -q 'Usage: ./pgmTile inputImage.pgm tiling_factor outputImage_<row>_<column>.pgm' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: Usage: ./pgmTile inputImage.pgm tiling_factor outputImage_<row>_<column>.pgm"
    echo "ACTUAL  : \c" 
    ./pgmTile



    echo "\n\npgmTile Wrong Argument Line"
    if  ./pgmTile WrongArgument | grep -q 'ERROR: Bad Argument Count' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Argument Count"
    echo "ACTUAL  : \c" 
    ./pgmTile WrongArgument



    echo "\n\npgmTile Input Non-numeric Tile Number"
    if  ./pgmTile ./ASCIIfile/slice0a.pgm nonNumeric output.pgm | grep -q 'ERROR: Miscellaneous' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Miscellaneous (The division factor must be a positive integer)"
    echo "ACTUAL  : \c" 
    ./pgmTile ./ASCIIfile/slice0a.pgm nonNumeric output.pgm



    echo "\n\npgmTile Input negative Tile Number"
    if  ./pgmTile ./ASCIIfile/slice0a.pgm -1 output.pgm | grep -q 'ERROR: Miscellaneous' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Miscellaneous (The division factor must be a positive integer)"
    echo "ACTUAL  : \c" 
    ./pgmTile ./ASCIIfile/slice0a.pgm -1 output.pgm



    echo "\n\npgmTile Output File Name should contain <row> and <column>"
    if  ./pgmTile ./ASCIIfile/slice0a.pgm 1 output.pgm | grep -q 'ERROR: Miscellaneous' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Miscellaneous (Bad Template)"
    echo "ACTUAL  : \c" 
    ./pgmTile ./ASCIIfile/slice0a.pgm 1 output.pgm



    echo "\n\npgmTile Bad file Name"
    if  ./pgmTile wrongFileName 5 'output_<row>_<column>.pgm' | grep -q 'ERROR: Bad File Name' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad File Name (wrongFileName)"
    echo "ACTUAL  : \c" 
    ./pgmTile wrongFileName 5 'output_<row>_<column>.pgm'



    echo "\n\npgmTile Bad Comment Line"
    if  ./pgmTile ./ASCIIfile/badCommentLine.pgm 5 'output_<row>_<column>.pgm' | grep -q 'ERROR: Bad Comment Line' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Comment Line (./ASCIIfile/badCommentLine.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmTile ./ASCIIfile/badCommentLine.pgm 5 'output_<row>_<column>.pgm'



    echo "\n\npgmTile Bad Magic Number"
    if  ./pgmTile ./ASCIIfile/badMagicNumber.pgm 5 'output_<row>_<column>.pgm' | grep -q 'ERROR: Bad Magic Number' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Magic Number (./ASCIIfile/badMagicNumber.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmTile ./ASCIIfile/badMagicNumber.pgm 5 'output_<row>_<column>.pgm'



    echo "\n\npgmTile Bad Dimension < 1"
    if  ./pgmTile ./ASCIIfile/badWidthDimension.pgm 5 'output_<row>_<column>.pgm' | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./ASCIIfile/badWidthDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmTile ./ASCIIfile/badWidthDimension.pgm 5 'output_<row>_<column>.pgm'



    echo "\n\npgmTile Bad Dimension > 65536"
    if  ./pgmTile ./ASCIIfile/badHeightDimension.pgm 5 'output_<row>_<column>.pgm' | grep -q 'ERROR: Bad Dimensions' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Dimensions (./ASCIIfile/badHeightDimension.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmTile ./ASCIIfile/badHeightDimension.pgm 5 'output_<row>_<column>.pgm'



    echo "\n\npgmTile Bad Max Gray Value"
    if  ./pgmTile ./ASCIIfile/badMaxGray.pgm 5 'output_<row>_<column>.pgm' | grep -q 'ERROR: Bad Max Gray Value' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Max Gray Value (./ASCIIfile/badMaxGray.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmTile ./ASCIIfile/badMaxGray.pgm 5 'output_<row>_<column>.pgm'



    echo "\n\npgmTile Too Little Data"
    if  ./pgmTile ./ASCIIfile/TooLittleData.pgm 5 'output_<row>_<column>.pgm' | grep -q 'ERROR: Bad Data' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Data (./ASCIIfile/TooLittleData.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmTile ./ASCIIfile/TooLittleData.pgm 5 'output_<row>_<column>.pgm'



    echo "\n\npgmTile Too Much Data"
    if  ./pgmTile ./ASCIIfile/TooMuchData.pgm 5 'output_<row>_<column>.pgm' | grep -q 'ERROR: Bad Data' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Data (./ASCIIfile/TooMuchData.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmTile ./ASCIIfile/TooMuchData.pgm 5 'output_<row>_<column>.pgm'



    echo "\n\npgmTile Output File format should be _<row>_<column>.pgm"
    if  ./pgmTile ./ASCIIfile/slice0a.pgm 5 'output<row><column>.pgm' | grep -q 'ERROR: Output Failed' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Output Failed (output<row><column>.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmTile ./ASCIIfile/slice0a.pgm 5 'output<row><column>.pgm'



    echo "\n\npgmTile Tile ASCII File Successfully"
    if  ./pgmTile ./ASCIIfile/slice0a.pgm 2 './ASCIIfile/TileSlice_<row>_<column>.pgm' | grep -q 'TILED' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: TILED"
    echo "ACTUAL  : \c" 
    ./pgmTile ./ASCIIfile/slice0a.pgm 2 './ASCIIfile/TileSlice_<row>_<column>.pgm'



    echo "\n\npgmTile Tile Binary File Successfully"
    if  ./pgmTile ./BinaryFile/baboon.pgm 5 './BinaryFile/TileBaboon_<row>_<column>.pgm' | grep -q 'TILED' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: TILED"
    echo "ACTUAL  : \c" 
    ./pgmTile ./BinaryFile/baboon.pgm 5 './BinaryFile/TileBaboon_<row>_<column>.pgm'

    echo "\n"
else
    echo "\npgmTile file does not exist"
    echo "                                                                                                                                      FAILED"
    : $((counter++)); 
fi

echo "______________________________________________________________________________________________________________________________________________\n"

FILE=pgmAssemble.c
if test -f "$FILE";
then echo "\npgmAssemble file exist"
    echo "                                                                                                                                      PASSED"
    echo "pgmAssemble No Argument"
    if  ./pgmAssemble | grep -q 'Usage: ./pgmAssemble outputImage.pgm width height (row column inputImage.pgm)+' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: Usage: ./pgmAssemble outputImage.pgm width height (row column inputImage.pgm)+"
    echo "ACTUAL  : \c" 
    ./pgmAssemble



    echo "\n\npgmAssemble Wrong Argument Line"
    if  ./pgmAssemble WrongArgument | grep -q 'ERROR: Bad Argument Count' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Argument Count"
    echo "ACTUAL  : \c" 
    ./pgmAssemble WrongArgument



    echo "\n\npgmAssemble Wrong Argument number"
    if  ./pgmAssemble ./ASCIIfile/Assemble.pgm 5 5 WrongArgument | grep -q 'ERROR: Bad Argument Count' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Bad Argument Count"
    echo "ACTUAL  : \c" 
    ./pgmAssemble ./ASCIIfile/Assemble.pgm 5 5 WrongArgument



    echo "\n\npgmAssemble Width and Height should be positibe integer"
    if  ./pgmAssemble ./ASCIIfile/Assemble.pgm -1 -1 | grep -q 'ERROR: Miscellaneous ' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Miscellaneous (The Assemble file width and height must be a positive integer)"
    echo "ACTUAL  : \c" 
    ./pgmAssemble ./ASCIIfile/Assemble.pgm -1 -1


    echo "\n\npgmAssemble Wrong Output File name"
    if  ./pgmAssemble ./WrongFile/Cannotoutput.pgm 4 4 0 0 ./ASCIIfile/slice0a.pgm 0 2 ./ASCIIfile/slice0a.pgm 2 0 ./ASCIIfile/slice0a.pgm 2 2 ./ASCIIfile/slice0a.pgm | grep -q 'ERROR: Output Failed' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ERROR: Output Failed (./WrongFile/Cannotoutput.pgm)"
    echo "ACTUAL  : \c" 
    ./pgmAssemble ./WrongFile/Cannotoutput.pgm 4 4 0 0 ./ASCIIfile/slice0a.pgm 0 2 ./ASCIIfile/slice0a.pgm 2 0 ./ASCIIfile/slice0a.pgm 2 2 ./ASCIIfile/slice0a.pgm


    echo "\n\npgmAssemble Successful Assemble ASCII File"
    if  ./pgmAssemble ./ASCIIfile/Assemble44.pgm 4 4 0 0 ./ASCIIfile/slice0a.pgm 0 2 ./ASCIIfile/slice0a.pgm 2 0 ./ASCIIfile/slice0a.pgm 2 2 ./ASCIIfile/slice0a.pgm | grep -q 'ASSEMBLED' ;
    then 
        echo "                                                                                                                                      PASSED"
    else 
        echo "                                                                                                                                      FAILED"
        : $((counter++)); 
    fi
    : $((counttest++));
    echo "EXPECTED: ASSEMBLED"
    echo "ACTUAL  : \c" 
    ./pgmAssemble ./ASCIIfile/Assemble44.pgm 4 4 0 0 ./ASCIIfile/slice0a.pgm 0 2 ./ASCIIfile/slice0a.pgm 2 0 ./ASCIIfile/slice0a.pgm 2 2 ./ASCIIfile/slice0a.pgm

    echo "\n"
else
    echo "\npgmAssemble file does not exist"
    echo "                                                                                                                                      FAILED"
    : $((counter++)); 
fi
echo "______________________________________________________________________________________________________________________________________________\n"
echo "Finish Testing                                                                                                               Total tests: $counttest "
echo "                                                                                                                                  FAILED: $counter\n\n"

make clean
