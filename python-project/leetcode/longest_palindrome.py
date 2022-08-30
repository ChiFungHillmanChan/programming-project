def main(s):
    if len(s) <= 1:
        return ''
    start, end = 0,0

    for i in range(len(s)):
        len1 = counter(s,i,i)
        len2 = counter(s,i,i+1)
        lenword = max(len1, len2)
        if (lenword > end - start):
            start = i - (lenword-1) // 2
            end = i + lenword//2
    return s[start:end+1]
def counter(s, left,right):
    L = left
    R = right
    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1
    return R-L-1

if __name__ == '__main__':
    print(main('cbbd'))