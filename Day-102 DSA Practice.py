# 693. Binary Number with Alternating Bits
# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)[2:]
        return all(bits[i] != bits[i + 1]
                   for i in range(len(bits) - 1))

# 740. Delete and Earn
# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        prev = curr = 0
        for x in range(max(freq) + 1):
            prev, curr = curr, max(curr, prev + x * freq[x])
        return curr
      
