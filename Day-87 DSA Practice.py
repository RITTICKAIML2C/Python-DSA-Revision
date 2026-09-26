# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
class Solution:
    def sortedSquares(self, nums):
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result

# 451. Sort Characters By Frequency
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
from collections import Counter
class Solution:
    def frequencySort(self, s):
        freq = Counter(s)
        return ''.join(
            ch * count
            for ch, count in freq.most_common()
        )     
