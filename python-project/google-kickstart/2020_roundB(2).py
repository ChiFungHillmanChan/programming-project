def solve():
    N,D = map(int, input().split())
    a = list(map(int, input().split()))
    ans = a[0] * int(D/a[0])
    if N == 1:
        return ans
    i = 1
    while i < N:
        if ans > (a[i] * int(D/a[i])):
            ans -= a[0]
        else:
            i += 1
        
    return ans
def main():
    t = int(float(input()))

    for i in range(1, t+1):
        ans = solve()
        print('Case #%s: %s' %(i, ans))


if __name__ == '__main__':
    main()