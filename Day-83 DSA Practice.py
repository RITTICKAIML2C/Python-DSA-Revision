# 448. Find All Numbers Disappeared in an Array
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        present = set(nums)
        return [i for i in range(1, n + 1) if i not in present]

# 309. Best Time to Buy and Sell Stock with Cooldown
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
class Solution:
    def maxProfit(self, prices):
        hold = -prices[0]
        sold = 0
        rest = 0
        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            hold = max(hold, rest - price)
            sold = prev_hold + price
            rest = max(rest, prev_sold)
        return max(sold, rest)
