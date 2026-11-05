# 1005. Maximize Sum Of Array After K Negations
# Given an integer array nums and an integer k, modify the array in the following way:
class Solution:
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
        if k % 2:
            nums.sort()
            nums[0] *= -1
        return sum(nums)

# 1094. Car Pooling
# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
class Solution:
    def carPooling(self, trips, capacity):
        changes = [0] * 1001
        for passengers, start, end in trips:
            changes[start] += passengers
            changes[end] -= passengers
        current = 0
        for change in changes:
            current += change
            if current > capacity:
                return False
        return True
      
