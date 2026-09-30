# 844. Backspace String Compare
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
class Solution:
    def backspaceCompare(self, s, t):
        def build(text):
            stack = []
            for ch in text:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return stack
        return build(s) == build(t)

# 72. Edit Distance
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # delete
                        dp[i][j - 1],      # insert
                        dp[i - 1][j - 1]  # replace
                    )
        return dp[m][n]
