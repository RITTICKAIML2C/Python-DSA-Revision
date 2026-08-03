# 40. Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sum to target.
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return result 

# 90. Subsets II
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []
        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return result
 
