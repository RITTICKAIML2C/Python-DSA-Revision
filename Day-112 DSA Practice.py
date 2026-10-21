# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
class Solution:
    def reverseString(self, s):
        s.reverse()

# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
class Solution:
    def generateParenthesis(self, n):
        res = []
        def backtrack(s, open_n, close_n):
            if len(s) == 2 * n:
                res.append(s)
                return
            if open_n < n:
                backtrack(s + "(", open_n + 1, close_n)
            if close_n < open_n:
                backtrack(s + ")", open_n, close_n + 1)
        backtrack("", 0, 0)
        return res
      
