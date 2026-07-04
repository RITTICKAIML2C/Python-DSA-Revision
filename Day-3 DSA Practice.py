# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in seen:
                return [seen[remaining], i]
            seen[nums[i]] = i

# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())
