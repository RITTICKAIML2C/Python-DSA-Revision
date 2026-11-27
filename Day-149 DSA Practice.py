# 1822. Sign of the Product of an Array
class Solution:
    def arraySign(self, nums):
        negative_count = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                negative_count += 1
        return 1 if negative_count % 2 == 0 else -1

# 1578. Minimum Time to Make Rope Colorful
class Solution:
    def minCost(self, colors, neededTime):
        total_cost = 0
        max_time = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                total_cost += min(max_time, neededTime[i])
                max_time = max(
                    max_time,
                    neededTime[i]
                )
            else:
                max_time = neededTime[i]
        return total_co


