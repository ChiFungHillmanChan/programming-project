"""
Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.
"""


"""
Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
"""
def dfs(n, num, k, res):
    if n == 0:
        return res.append(num)
    
    tail = num % 10
    next_digits = set([tail + k, tail - k])

    for next_digit in next_digits:
        if 0 <= next_digit < 10:
            new_num = num * 10 + next_digit
            dfs(n-1, new_num, k, res)

def main(n, k):
    res = []
    if n == 1:
        return [i for i in range(10)]
    for num in range(1, 10):
        dfs(n-1, num, k, res)

    return list(res)



if __name__ == '__main__':
    print(main(3, 7))
    print(main(2, 1))