# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
class Solution:
    def moveZeroes(self, nums):
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        while pos < len(nums):
            nums[pos] = 0
            pos += 1

# 714. Best Time to Buy and Sell Stock with Transaction Fee
# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
class Solution:
    def maxProfit(self, prices, fee):
        cash = 0
        hold = -prices[0]
        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash
