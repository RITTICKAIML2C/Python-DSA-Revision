# 387. First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        count = Counter(s)
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1

# 402. Remove K Digits
# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
class Solution:
    def removeKdigits(self, num, k):
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        if k:
            stack = stack[:-k]
        result = ''.join(stack).lstrip('0')
        return result or '0'
