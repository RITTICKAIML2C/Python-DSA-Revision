# 1027. Longest Arithmetic Subsequence
# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
class Solution:
    def longestArithSeqLength(self, nums):
        dp = [{} for _ in nums]
        ans = 2
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                ans = max(ans, dp[i][diff])
        return ans

# 1346. Check If N and Its Double Exist
# Given an array arr of integers, check if there exist two indices i and j such that
class Solution:
    def checkIfExist(self, arr):
        seen = set()
        for x in arr:
            if 2 * x in seen or (x % 2 == 0 and x // 2 in seen):
                return True
            seen.add(x)
        return False
      
