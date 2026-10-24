# 976. Largest Perimeter Triangle
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
class Solution:
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i:i + 3]
            if b + c > a:
                return a + b + c
        return 0

# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.
class Solution:
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
