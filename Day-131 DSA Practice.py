# 983. Minimum Cost For Tickets
# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.
class Solution:
    def mincostTickets(self, days, costs):
        travel = set(days)
        dp = [0] * 366
        for day in range(365, 0, -1):
            if day not in travel:
                dp[day] = dp[day + 1]
            else:
                dp[day] = min(
                    costs[0] + dp[day + 1],
                    costs[1] + dp[min(day + 7, 366)],
                    costs[2] + dp[min(day + 30, 366)]
                )
        return dp[1]

# 1608. Special Array With X Elements Greater Than or Equal X
# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
class Solution:
    def specialArray(self, nums):
        nums.sort()
        n = len(nums)
        for x in range(n + 1):
            count = n - (
                next((i for i, v in enumerate(nums) if v >= x), n)
            )
            if count == x:
                return x
        return -1
