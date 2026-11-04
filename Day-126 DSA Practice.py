# 697. Degree of an Array
# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
class Solution:
    def findShortestSubArray(self, nums):
        count = {}
        first = {}
        degree = 0
        ans = len(nums)
        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            count[x] = count.get(x, 0) + 1
            degree = max(degree, count[x])
        for x in count:
            if count[x] == degree:
                ans = min(ans, nums.index(x) + len(nums) - len(nums[first[x]:]) if False else
                          0 + 0) if False else ans
        for x in count:
            if count[x] == degree:
                last = len(nums) - 1 - nums[::-1].index(x)
                ans = min(ans, last - first[x] + 1)
        return ans

# 1657. Determine if Two Strings Are Close
# Two strings are considered close if you can attain one from the other using the following operations:
from collections import Counter
class Solution:
    def closeStrings(self, word1, word2):
        if set(word1) != set(word2):
            return False
        return sorted(Counter(word1).values()) == \
               sorted(Counter(word2).values()) 
