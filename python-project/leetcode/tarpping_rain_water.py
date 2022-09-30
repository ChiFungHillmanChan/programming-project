height = [4, 2, 0, 3, 2 , 5]

"""
Dynamic Programming algorithms

Time complexity: O(n)
store heights in 2 iteration of O(n) each
Then update ans in O(n)

Space complexity: O(n)
O(n) for left_max and right_max(array)

"""
def trapping_rain_water(height):
    if not height:
        return 0
        
    ans, size = 0, len(height)
    left_max , right_max = [0 for _ in range(size)], [0 for _ in range(size)]
    left_max[0] = height[0]
    
    for i in range(1, size):
        left_max[i] = max(height[i], left_max[i - 1])
    right_max[size-1] = height[size-1]
    for i in range(size-2, 0, -1):
        right_max[i] = max(height[i], right_max[i+1])
    for i in range(i, size-1):
        ans += min(left_max[i], right_max[i]) - height[i]
        
    return ans
if __name__ == '__main__':
    trapping_rain_water(height)