# 1356. Sort Integers by The Number of 1 Bits
class Solution:
    def sortByBits(self, arr):
        return sorted(
            arr,
            key=lambda x: (x.bit_count(), x)
        )

# 931. Minimum Falling Path Sum
class Solution:
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        dp = matrix[-1][:]
        for i in range(n - 2, -1, -1):
            new_dp = [0] * n
            for j in range(n):
                best = dp[j]
                if j > 0:
                    best = min(best, dp[j - 1])
                if j < n - 1:
                    best = min(best, dp[j + 1])
                new_dp[j] = matrix[i][j] + best
            dp = new_dp
        return min(dp)
