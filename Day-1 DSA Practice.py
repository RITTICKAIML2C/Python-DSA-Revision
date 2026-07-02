# Q : 1929. Concatenation of Array
# Easy
# Topics
# premium lock icon
# Companies
# Hint : Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed). Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.
class Solution:
    def getConcatenation(self, nums):
        return nums + nums

# Q : 3. Longest Substring Without Repeating Characters
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, find the length of the longest substring without duplicate characters.
class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = 0
        for i in range(len(s)):
            substring = ""
            for j in range(i, len(s)):
                if s[j] not in substring:
                    substring = substring + s[j]
                else:
                    break
            if len(substring) > longest:
                longest = len(substring)
        return longest
        
