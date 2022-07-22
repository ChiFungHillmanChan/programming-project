def solve():
    N = int(float(input()))
    a = list(map(int, input().split()))
    ans = 0
    if N <= 2:
        return ans
    for i in range(1, N-1):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            ans+=1
    return ans
def main():
    t = int(float(input()))
    for i in range(1, t+1):
        ans = solve()
        print('Case #{}: {}'.format(i, ans))

if __name__ == '__main__':
    main()