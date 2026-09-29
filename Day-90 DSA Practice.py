# 485. Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        current = 0
        best = 0
        for x in nums:
            if x == 1:
                current += 1
                best = max(best, current)
            else:
                current = 0
        return best

# 621. Task Scheduler
# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n
from collections import Counter
def leastInterval(tasks, n):
    freq = Counter(tasks)
    max_freq = max(freq.values())
    slots = (max_freq - 1) * (n + 1)
    slots += sum(v == max_freq for v in freq.values())
    return max(len(tasks), slots)
