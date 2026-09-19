# 1539. Kth Missing Positive Number
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Return the kth positive integer that is missing from this array.
class Solution:
    def findKthPositive(self, arr, k):
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k

# 380. Insert Delete GetRandom O(1)
# You must implement the functions of the class such that each function works in average O(1) time complexity.
import random
class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.pos = {}
    def insert(self, val):
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True
    def remove(self, val):
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.pos[last] = idx
        self.nums.pop()
        del self.pos[val]
        return True
    def getRandom(self):
        return random.choice(self.nums)
