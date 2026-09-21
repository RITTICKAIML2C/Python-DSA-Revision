# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
class Solution:
    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans

# 300. Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
