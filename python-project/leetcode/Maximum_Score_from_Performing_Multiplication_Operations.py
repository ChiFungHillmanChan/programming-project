from audioop import mul


nums = [-5, -3, -3, -2, 7, 1]
multipliers = [-10, -5, 3, 4, 6]

def main(nums, multipliers):
    m = len(multipliers)
    n = len(nums)

    memo = {}

    def dp(op, left):
        if op == m:
            return 0
            
        if (op, left) in memo:
            return memo[(op, left)]

        right = ( n-1 ) - (op-left)
        l = nums[left] * multipliers[op] + dp(op+1, left+1)
        r = nums[right] * multipliers[op] + dp(op+1, left)

        return memo[(op, left)]

    return dp(0, 0)

if __name__ == '__main__':
    main(nums, multipliers)
