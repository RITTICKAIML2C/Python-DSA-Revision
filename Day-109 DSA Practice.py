# 896. Monotonic Array
# An array is monotonic if it is either monotone increasing or monotone decreasing.
class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        inc = all(nums[i] <= nums[i + 1]
                  for i in range(len(nums) - 1))
        dec = all(nums[i] >= nums[i + 1]
                  for i in range(len(nums) - 1))
        return inc or dec

# 213. House Robber II
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police
class Solution:
    def rob(self, nums: list[int]) -> int:
        def linear(arr):
            prev = curr = 0
            for x in arr:
                prev, curr = curr, max(curr, prev + x)
            return curr
        if len(nums) == 1:
            return nums[0]
        return max(linear(nums[:-1]), linear(nums[1:]))
