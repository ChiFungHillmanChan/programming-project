def solve():
    N,K= map(int, input().split())
    a = list(map(int, input().split()))

    lb = 1
    rb = a[N-1] - a[0]
    while (lb < rb):
        mb = (lb+rb)/2
        k2 = 0
        for i in range(1, N):
            d = a[i] - a[i-1]
            k2 += (d+mb-1)/mb -1
        if k2<= K:
            rb = mb
        else:
            lb = mb+1
    return int(lb)

def main():
    t = int(float(input()))
    n = 1
    while(n <= t):
        ans = solve()
        print('Case #%s: %s' %(n, ans))
        n+=1

if __name__ == '__main__':
    main()