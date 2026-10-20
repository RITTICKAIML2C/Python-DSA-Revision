# 240. Search a 2D Matrix II
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            value = matrix[row][col]
            if value == target:
                return True
            elif value > target:
                col -= 1
            else:
                row += 1
        return False

# 905. Sort Array By Parity
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
class Solution:
    def sortArrayByParity(self, nums):
        return [x for x in nums if x % 2 == 0] + \
               [x for x in nums if x % 2 != 0]
      
