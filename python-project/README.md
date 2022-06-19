# Python Projects

This directory includes all my Python projects. This page will show you what are the python project is doing.

## check-polindrome.py

This python program is going to check if the string input is palindrome
- palindrome means the word will be the same if it is reversed
- For example, string "level" is palindrome. 

In this program, only string will be detected and it will automatically transform to lower case. 
- For example, if you input "le /V/ @eL" the output will consider it to be "level"

And return True or False


## valid-subsequence.py

This program is to check if required list is the subsequence of the main list

Two ArrayList will be inputted and the program will run. 
It will check if:
1. Subsequence is in main row
```python
main:[1,2,3,4,5]
subsequence:[2,3]

# This will return True as [2,3] is a subsequence of main 
```


2. Subsequence is in correct order
```python
main:[1,2,3,4,5]
subsequence:[3,2]

# This will return False as [3, 2] is not in correct order of main 
```


3. check repeated
```python
main:[1,2,3,4,5]
subsequence:[2 ,2, 3]

# This will return False as subsequence has two '2's but main has only one 
```