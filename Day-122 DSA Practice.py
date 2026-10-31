# 1295. Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits.
class Solution:
    def findNumbers(self, nums):
        return sum(len(str(x)) % 2 == 0 for x in nums)


# 416. Partition Equal Subset Sum
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = {0}
        for num in nums:
            dp |= {x + num for x in dp if x + num <= target}
        return target in dp
