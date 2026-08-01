# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
class Solution:
    def permute(self, nums):
        result = []
        def backtrack(path, remaining):
            if not remaining:
                result.append(path)
                return
            for i in range(len(remaining)):
                backtrack(
                    path + [remaining[i]],
                    remaining[:i] + remaining[i + 1:]
                )
        backtrack([], nums)
        return result

# 78. Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
class Solution:
    def subsets(self, nums):
        result = []
        def backtrack(index, subset):
            if index == len(nums):
                result.append(subset[:])
                return
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()
            backtrack(index + 1, subset)
        backtrack(0, [])
        return result
