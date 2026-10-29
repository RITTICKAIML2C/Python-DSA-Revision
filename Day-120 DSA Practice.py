# 1071. Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
from math import gcd
class Solution:
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]

# 930. Binary Subarrays With Sum
# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums, goal):
        freq = defaultdict(int)
        freq[0] = 1
        total = ans = 0
        for x in nums:
            total += x
            ans += freq[total - goal]
            freq[total] += 1
        return ans
