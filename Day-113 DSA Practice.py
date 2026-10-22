# 645. Set Mismatch
# You have a set of integers s, which originally contains all the numbers from 1 to n.
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        duplicate = sum(nums) - sum(set(nums))
        missing = n * (n + 1) // 2 - sum(set(nums))
        return [duplicate, missing]

# 73. Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
class Solution:
    def setZeroes(self, matrix):
        rows = {i for i, row in enumerate(matrix) if 0 in row}
        cols = {j for j in range(len(matrix[0]))
                if any(matrix[i][j] == 0 for i in range(len(matrix)))}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
