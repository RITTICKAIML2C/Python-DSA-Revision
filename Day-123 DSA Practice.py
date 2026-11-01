# 1512. Number of Good Pairs
# Given an array of integers nums, return the number of good pairs.
class Solution:
    def numIdenticalPairs(self, nums):
        freq = {}
        ans = 0
        for x in nums:
            ans += freq.get(x, 0)
            freq[x] = freq.get(x, 0) + 1
        return ans

# 1423. Maximum Points You Can Obtain from Cards
# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
class Solution:
    def maxScore(self, cardPoints, k):
        total = sum(cardPoints)
        window = len(cardPoints) - k
        if window == 0:
            return total
        curr = sum(cardPoints[:window])
        minimum = curr
        for i in range(window, len(cardPoints)):
            curr += cardPoints[i] - cardPoints[i - window]
            minimum = min(minimum, curr)
        return total - minimum



