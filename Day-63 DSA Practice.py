# 441. Arranging Coins
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.
class Solution:
    def arrangeCoins(self, n):
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            coins = mid * (mid + 1) // 2
            if coins == n:
                return mid
            if coins < n:
                left = mid + 1
            else:
                right = mid - 1
        return right

# 525. Contiguous Array
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
class Solution:
    def findMaxLength(self, nums):
        first_seen = {0: -1}
        prefix = 0
        longest = 0
        for i, num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1
            if prefix in first_seen:
                longest = max(
                    longest,
                    i - first_seen[prefix]
                )
            else:
                first_seen[prefix] = i
        return longest

  
