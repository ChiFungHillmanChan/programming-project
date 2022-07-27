def solve():
    T,K = map(int, input().split())
    a = list(map(int, input().split()))
    check = K
    ans = 0
    for i in a:
        if i == check:
            check -= 1
            if check == 0:
                ans += 1
                check = K
        else:
            check = K
    return ans
def main():
    t = int(float(input()))
    for i in range(1, t+1):
        ans = solve()
        print('Case #%s: %s' %(i, ans))
if __name__ == '__main__':
    main()