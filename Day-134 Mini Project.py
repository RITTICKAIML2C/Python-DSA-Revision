# 1502. Can Make Arithmetic Progression From Sequence
# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
class Solution:
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        difference = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != difference:
                return False
        return True

# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        current_sum = 0
        min_length = float('inf')
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(
                    min_length,
                    right - left + 1
                )
                current_sum -= nums[left]
                left += 1
        return 0 if min_length == float('inf') else min_length
