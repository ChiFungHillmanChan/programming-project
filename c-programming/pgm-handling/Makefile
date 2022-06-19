CC=gcc

CCFLAGS=	-g	-std=c99

MODULES=	pgmReadAndWrite.o	pgmError.o	pgmConvert.o	

MAINS=	pgmEcho.o	pgmComp.o	pgma2b.o	pgmb2a.o	pgmConvert.o	pgmReduce.o	pgmTile.o	pgmAssemble.o

TARGETS=	pgmEcho	pgmComp	pgma2b	pgmb2a	pgma2b	pgmb2a	pgmReduce	pgmTile	pgmAssemble

all:	${TARGETS}

clean:
	rm	-f	${TARGETS}	${MAINS}	${MODULES}	*.o

pgmEcho:		pgmEcho.o	${MODULES}
	${CC}	${CCFLAGS}		-o	pgmEcho	pgmEcho.o	${MODULES}
			
pgmComp:		pgmComp.o	${MODULES}
	${CC}	${CCFLAGS}		-o	pgmComp	pgmComp.o	${MODULES}	

pgma2b:			pgma2b.o	${MODULES}
	${CC}	${CCFLAGS}		-o	pgma2b	pgma2b.o	${MODULES}	

pgmb2a:			pgmb2a.o	${MODULES}
	${CC}	${CCFLAGS}		-o	pgmb2a	pgmb2a.o	${MODULES}

pgmReduce:			pgmReduce.o	${MODULES}
	${CC}	${CCFLAGS}		-o	pgmReduce	pgmReduce.o	${MODULES}

pgmTile:			pgmTile.o	${MODULES}
	${CC}	${CCFLAGS}		-o	pgmTile	pgmTile.o	${MODULES}

pgmAssemble:			pgmAssemble.o	${MODULES}
	${CC}	${CCFLAGS}		-o	pgmAssemble	pgmAssemble.o	${MODULES}

pgmEcho.o: 		pgmEcho.c 	pgmStructure.h	pgmError.h	pgmReadAndWrite.h		
	${CC}	-c	${CCFLAGS}	-o	pgmEcho.o	pgmEcho.c 

pgmReadAndWrite.o:	pgmReadAndWrite.c	pgmStructure.h	pgmError.h	pgmReadAndWrite.h 	
	${CC}	-c	${CCFLAGS}	-o	pgmReadAndWrite.o	pgmReadAndWrite.c 

pgmError.o:		pgmError.c	pgmStructure.h	pgmError.h
	${CC}	-c	${CCFLAGS}	-o	pgmError.o	pgmError.c
	
pgmComp.o:		pgmComp.c 	pgmStructure.h	pgmError.h	pgmReadAndWrite.h	pgmConvert.h	pgmComp.h
	${CC}	-c	${CCFLAGS}	-o	pgmComp.o	pgmComp.c 

pgma2b.o: 		pgma2b.c 	pgmStructure.h	pgmError.h	pgmReadAndWrite.h	pgmConvert.h		
	${CC}	-c	${CCFLAGS}	-o	pgma2b.o	pgma2b.c 

pgmb2a.o:		pgmb2a.c 	pgmStructure.h	pgmError.h	pgmReadAndWrite.h	pgmConvert.h
	${CC}	-c	${CCFLAGS}	-o	pgmb2a.o	pgmb2a.c 

pgmConvert.o:	pgmConvert.c 	pgmStructure.h	pgmError.h	pgmReadAndWrite.h	pgmConvert.h
	${CC}	-c	${CCFLAGS}	-o	pgmConvert.o	pgmConvert.c 

pgmReduce.o:	pgmReduce.c 	pgmStructure.h	pgmError.h	pgmReadAndWrite.h	pgmReduce.h
	${CC}	-c	${CCFLAGS}	-o	pgmReduce.o	pgmReduce.c 

pgmTile.o:	pgmTile.c 	pgmStructure.h	pgmError.h	pgmReadAndWrite.h	pgmTile.h
	${CC}	-c	${CCFLAGS}	-o	pgmTile.o	pgmTile.c 

pgmAssemble.o:	pgmAssemble.c 	pgmStructure.h	pgmError.h	pgmReadAndWrite.h	pgmAssemble.h
	${CC}	-c	${CCFLAGS}	-o	pgmAssemble.o	pgmAssemble.c 