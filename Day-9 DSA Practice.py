# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Example 1: Input: s = "()", Output: true
class Solution:
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != pairs[ch]:
                    return False
        return len(stack) == 0

# 155. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Input - ["MinStack","push","push","push","getMin","pop","top","getMin"], [[],[-2],[0],[-3],[],[],[],[]]
# Output - [null,null,null,null,-3,null,0,-2]
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val):
        self.stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min_stack[-1]
