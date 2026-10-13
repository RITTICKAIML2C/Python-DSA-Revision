# 404. Sum of Left Leaves
# Given the root of a binary tree, return the sum of all left leaves.
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if not root:
            return 0
        total = 0
        if root.left:
            if not root.left.left and not root.left.right:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        return total

# 221. Maximal Square
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        largest = 0
        for i in range(1, rows + 1):
            diagonal = 0
            for j in range(1, cols + 1):
                old = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = 1 + min(
                        dp[j], dp[j - 1], diagonal
                    )
                    largest = max(largest, dp[j])
                else:
                    dp[j] = 0
                diagonal = old
        return largest * largest
