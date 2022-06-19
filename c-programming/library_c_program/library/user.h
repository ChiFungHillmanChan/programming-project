void listAvailableBooks( Book *bookList, int numBooks );
void borrowBook( User *theUser, Book *bookList, int numBooks, int maxBorrowed );

void listMyBooks( User *theUser, Book *bookList, int maxBorrowed );
void returnBook( User *theUser, Book *bookList, int numBooks, int maxBorrowed );

void userCLI( Library *theLibrary );
