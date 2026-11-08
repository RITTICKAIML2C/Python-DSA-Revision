# 1450. Number of Students Doing Homework at a Given Time
# Given two integer arrays startTime and endTime and given an integer queryTime.
class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                count += 1
        return count


# 1658. Minimum Operations to Reduce X to Zero
# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
class Solution:
    def minOperations(self, nums, x):
        target = sum(nums) - x
        seen = {0: -1}
        total = 0
        longest = -1
        for i, num in enumerate(nums):
            total += num
            if total - target in seen:
                longest = max(longest, i - seen[total - target])
            seen.setdefault(total, i)
        return len(nums) - longest if longest != -1 else -1


