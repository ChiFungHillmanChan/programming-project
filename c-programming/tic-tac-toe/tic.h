//#define TEST				// uncomment this #define directive to run the grader on your machine

// PLEASE DON'T UPLOAD THIS FILE TO THE AUTOGRADER.
//-------------------------------------------------

// ********************************************************************************************************************
// DO NOT CHANGE ANYTHING IN THE FOLLOWING SECTION. IF YOU CHANGE ANYTHING, YOUR CODE WILL FAIL THE AUTOGRADER TESTS.
// However, please read through this section and look at declarations of data and functions that you will use in your code

#define MaxGrid 10					// the maximum size of the game's grid
extern char grid[MaxGrid][MaxGrid];	// the game's grid

// prototypes of the functions that you will implementing
// the functions themselves are in the tic.c file
int newGame (int gridsize, int winlength);
int makeMove(int row, int col, char symbol);
int boardIsFull();
int checkHorizontal (char symbol, int length);
int checkVertical (char symbol, int length);
int checkDiagonals (char symbol, int length);
int checkAntiDiagonals (char symbol, int length);
int playerHasWon (char symbol , int length);
int effPlayerHasWon (int row, int col, char symbol , int length);
void showGrid ();

int check (int row, int col, char symbol);  // use this function in effPlayerHasWon. Don't redefine the function, it is already defined in the grader

// do NOT use or redefine any of the following functions, it is for the grader only
int peek (int row, int col);	// do not use this function, it is for the grader only
extern int __Check_Count;		// do not use this variable, it is for the grader only
extern int IsAutoGradinng;      // do not use this variable, it is for the grader only

// END OF CODE SECTION THAT SHOULD NOT BE CHANGED
// ************************************************