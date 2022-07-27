def reverse(x):
    sign = -1 if x < 0 else 1
    x *= sign
    while x:
        if x % 10 == 0:
            x/=10
        else:
            break
    a = list(str(x))
    a.reverse()
    x = int("".join(a))
    if x < - 2**31 or x > (2**31 - 1):
        return 0
    return sign*x

reverse(123)