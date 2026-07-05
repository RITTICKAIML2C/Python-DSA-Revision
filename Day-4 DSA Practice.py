# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.
class Solution:
    def searchRange(self, nums, target):
        first = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]
