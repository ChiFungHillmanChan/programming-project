def solve():
    n,b = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for house in a:
        if b >= house:
            b -= house
            ans += 1
        else:
            break
    return ans



def main():
    t = int(float(input()))
    n = 1
    while(n <= t):
        ans = solve()
        print('Case #%s: %s' %(n, ans))
        n+=1

if __name__ == '__main__':
    main()