# 599. Minimum Index Sum of Two Lists
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
class Solution:
    def findRestaurant(self, list1, list2):
        pos = {word: i for i, word in enumerate(list1)}
        best = float("inf")
        result = []
        for j, word in enumerate(list2):
            if word in pos:
                total = pos[word] + j
                if total < best:
                    best = total
                    result = [word]
                elif total == best:
                    result.append(word)
        return result

# 377. Combination Sum IV
# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for total in range(1, target + 1):
            for num in nums:
                if num <= total:
                    dp[total] += dp[total - num]
        return dp[target]    
