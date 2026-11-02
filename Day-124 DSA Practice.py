# 674. Longest Continuous Increasing Subsequence
# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
class Solution:
    def findLengthOfLCIS(self, nums):
        best = curr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                curr = 1
            best = max(best, curr)
        return best if nums else 0
