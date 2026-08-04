# 216. Combination Sum III
# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# Only numbers 1 through 9 are used. Each number is used at most once.
class Solution:
    def combinationSum3(self, k, n):
        result = []
        def backtrack(start, path, total):
            if len(path) == k:
                if total == n:
                    result.append(path[:])
                return
            for num in range(start, 10):
                path.append(num)
                backtrack(num + 1, path, total + num)
                path.pop()
        backtrack(1, [], 0)
        return result

# 131. Palindrome Partitioning
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
class Solution:
    def partition(self, s):
        result = []
        def isPalindrome(text):
            return text == text[::-1]
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                part = s[start:end]
                if isPalindrome(part):
                    path.append(part)
                    backtrack(end, path)
                    path.pop()
        backtrack(0, [])
        return result
