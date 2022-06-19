
typedef struct _book {

  char title[40];
  char author[40];
  int available;

} Book;

typedef struct _user {

  Book *borrowed[4];
  int numBorrowed;

} User;

typedef struct _library {

  Book *bookList;
  int numBooks;
  int maxBooks;

  User theUser;
  int maxBorrowed;

} Library;

