# Python Projects

This directory includes all my Python projects. This page will show you what are the python project is doing.

Link to description:
link:(##-two_sum.py)

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

## roulette.py

This is a fun project to play with Roulette. Player can input the deposit and start the game.

This function imports time and random. 
```python
import time
import random
```

the roulette will auto spin after required TIME. But player can use keyboard to interrupt it

The function is not fully finished yet. It is functionable but still can be improved

## ugly_number.py

requirement for ugly number:

Programming challenge description:
Credits: This challenge has appeared in a google competition.

Once upon a time in a strange situation, people called a number ugly if it was divisible by any of the one-digit primes (2, 3, 5 or 7). Thus, 14 is ugly, but 13 is fine. 39 is ugly, but 121 is not. Note that 0 is ugly. Also note that negative numbers can also be ugly; -14 and -39 are examples of such numbers.

One day on your free time, you are gazing at a string of digits, something like:
123456
You are amused by how many possibilities there are if you are allowed to insert plus or minus signs between the digits. For example you can make:

1 + 234 - 5 + 6 = 236
which is ugly. Or
123 + 4 - 56 = 71
which is not ugly.

It is easy to count the number of different ways you can play with the digits: Between each two adjacent digits you may choose put a plus sign, a minus sign, or nothing. Therefore, if you start with D digits there are 3^(D-1) expressions you can make. Note that it is fine to have leading zeros for a number. If the string is '01023', then '01023', '0+1-02+3' and '01-023' are legal expressions.

Your task is simple: Among the 3^(D-1) expressions, count how many of them evaluate to an ugly number.
Input:
Your program should read lines of text from standard input. Each line will consist of a non-empty string containing only the characters '0' through '9'. Each string is no more than 13 characters long.
Output:
For each input string, print to standard output the number of expressions that evaluate to an ugly number, one number per line.

## two_sum.py
This is a problem from 'Leetcode'

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

## roman_to_integer.py
This is a problem from 'Leetcode' to input the roman number and return it by integer.

## linked_list.py
This is a program to work with linked list in python
This file just work with append, prepend and insert to specific place



