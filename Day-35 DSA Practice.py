# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        phone = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        result = []
        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return
            for ch in phone[digits[index]]:
                backtrack(index + 1, path + ch)
        backtrack(0, "")
        return result

# 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != word[i]):
                return False
            temp = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            board[r][c] = temp
            return found
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
 
