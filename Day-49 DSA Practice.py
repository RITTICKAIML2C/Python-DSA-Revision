# 219. Contains Duplicate II
# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False

# 503. Next Greater Element II
# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(2 * n):
            index = i % n
            while stack and nums[stack[-1]] < nums[index]:
                result[stack.pop()] = nums[index]
            if i < n:
                stack.append(index)
        return result
