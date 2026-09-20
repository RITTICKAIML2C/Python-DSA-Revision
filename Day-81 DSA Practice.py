# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string.
class Solution:
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]

# 279. Perfect Squares
# Given an integer n, return the least number of perfect square numbers that sum to n.
class Solution:
    def numSquares(self, n):
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]
