# 944. Delete Columns to Make Sorted
# You are given an array of n strings strs, all of the same length.
class Solution:
    def minDeletionSize(self, strs):
        return sum(
            any(strs[i][j] > strs[i + 1][j]
                for i in range(len(strs) - 1))
            for j in range(len(strs[0]))
        )

# 287. Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
class Solution:
    def findDuplicate(self, nums):
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
