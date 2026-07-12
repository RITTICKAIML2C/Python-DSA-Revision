# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day
# Example 1: Input: prices = [7,1,5,3,6,4]
# Output: 5
class Solution:
    def maxProfit(self, prices):
        minimum_price = prices[0]
        maximum_profit = 0
        for price in prices:
            if price < minimum_price:
                minimum_price = price
            profit = price - minimum_price
            if profit > maximum_profit:
                maximum_profit = profit
        return maximum_profit

# 739. Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
# Example 1: Input: temperatures = [73,74,75,71,69,72,76,73], Output: [1,1,4,2,1,1,0,0]
class Solution:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        return answer
