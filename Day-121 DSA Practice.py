# 1207. Unique Number of Occurrences
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr):
        freq = Counter(arr)
        return len(freq.values()) == len(set(freq.values()))

# 494. Target Sum
# You are given an integer array nums and an integer target.
class Solution:
    def findTargetSumWays(self, nums, target):
        dp = {0: 1}
        for num in nums:
            new = {}
            for total, count in dp.items():
                new[total + num] = new.get(total + num, 0) + count
                new[total - num] = new.get(total - num, 0) + count
            dp = new
        return dp.get(target, 0)

  
