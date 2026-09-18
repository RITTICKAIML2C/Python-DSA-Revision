# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums) 

# 75. Sort Colors
# You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
class Solution:
    def sortColors(self, nums):
        low = mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
