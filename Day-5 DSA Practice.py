# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1: Input: s = "anagram", t = "nagaram", Output: true
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

# 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k. A subarray is a contiguous non-empty sequence of elements within an array.
# Example 1: Input: nums = [1,1,1], k = 2, Output: 2
class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        prefix_count = {0: 1}
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in prefix_count:
                count += prefix_count[prefix_sum - k]
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum] = 1
        return count
