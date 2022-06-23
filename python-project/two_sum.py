def main(nums, target):
    index = 0
    while index <len(nums):
        for num in range(len(nums)):
            if nums[index] + nums[num] == target and index != num:
                return [index, num]
        index += 1