
def solve():
    N,K,P = map(int, input().split())

    #set 2d array for a
    a = [[] for _ in range(N)]
    for i in range(N):
        a[i] = list(map(int, input().split()))
    
    #set 2d
    sum = [[ 0 for _ in range(K+1) ] for _ in range(N+1)]
    for z in range(1,N+1):
        for y in range(1,K+1):
            sum[z][y] = sum[z][y-1] + a[z-1][y-1]
    print ('\n\n')
    dp = [[ 0 for _ in range(P+1) ] for _ in range(N+1)]
    for m in range(1, N+1):
        for n in range(1, P+1):
            dp[m][n] = 0
            print('loop {}{}'.format(m,n))
            for x in range((min(n,K))+1):
                print('min = {}, m = {}, n = {}, x = {}, dp[m][n] = {} , sum[m][x] + dp[m-1][n-x] = {}, max = {}'.format((min(n,K)+1),m,n,x, dp[m][n],sum[m][x]+ dp[m-1][n-x],max(dp[m][n], sum[m][x] + dp[m-1][n-x])))
                dp[m][n] = max(dp[m][n], sum[m][x] + dp[m-1][n-x])
            print ('\n')
            for i in range(len(dp)):
                print (dp[i])

    for i in range(len(sum)):
        print (sum[i])

    
    return dp[N][P]


# 10 10 100 30
# 80 50 10 50 
def main():
    t = int(float(input()))
    n = 1
    while(n <= t):
        ans = solve()
        print('Case #{}: {}' .format(n, ans))
        n+=1

if __name__ == '__main__':
    main()