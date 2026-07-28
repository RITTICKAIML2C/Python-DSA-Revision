# 69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well.
class Solution:
    def mySqrt(self, x):
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

# 153. Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# For example, the array nums = [0,1,2,4,5,6,7] might become
class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left] 
