# 26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Example 1: Input: nums = [1,1,2], Output: 2, nums = [1,2,_]
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

# 36. Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                box = (i // 3) * 3 + (j // 3)
                if value in rows[i]:
                    return False
                if value in cols[j]:
                    return False
                if value in boxes[box]:
                    return False
                rows[i].add(value)
                cols[j].add(value)
                boxes[box].add(value)
        return True
