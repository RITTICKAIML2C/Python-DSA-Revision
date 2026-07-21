# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        first = 1
        second = 2
        for i in range(3, n + 1):
            first, second = second, first + second
        return second

# 198. House Robber
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
class Solution:
    def rob(self, nums):
        rob1 = 0
        rob2 = 0
        for money in nums:
            newRob = max(rob1 + money, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
