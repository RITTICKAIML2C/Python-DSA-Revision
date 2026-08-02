# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.
class Solution:
    def combine(self, n, k):
        result = []
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        backtrack(1, [])
        return result

# 39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return result
