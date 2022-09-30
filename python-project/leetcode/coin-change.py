coins = [1,5,6,7]
amount = 15

def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    print (dp)
    print ('\n')
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                print ("dp[a]:",dp[a],"   a:",a,"   c:", c,"   a-c:", a-c , "   dp[a-c] + 1:" , dp[a-c] + 1)
                dp[a] = min(dp[a], 1 + dp[a-c])

    return dp[amount] if dp[amount] != amount +1 else -1


if __name__ == '__main__':
    print (coinChange(coins, amount))
