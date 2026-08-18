# 567. Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        need = Counter(s1)
        window = Counter()
        left = 0
        for right in range(len(s2)):
            window[s2[right]] += 1
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            if window == need:
                return True
        return False

# 643. Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
class Solution:
    def findMaxAverage(self, nums, k):
        window = sum(nums[:k])
        maximum = window
        for i in range(k, len(nums)):
            window += nums[i]
            window -= nums[i - k]
            maximum = max(maximum, window)
        return maximum / k
