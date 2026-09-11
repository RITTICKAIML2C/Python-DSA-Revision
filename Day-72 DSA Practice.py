# 1143. Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        dp = [[0] * (len(text2) + 1)
              for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j],
                                   dp[i][j - 1])
        return dp[-1][-1]

# 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
class Solution:
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = result[i-1][j-1] + result[i-1][j]
            result.append(row)
        return result
