# 1217. Minimum Cost to Move Chips to The Same Position
# We have n chips, where the position of the ith chip is position[i].
class Solution:
    def minCostToMoveChips(self, position):
        odd = sum(x % 2 for x in position)
        even = len(position) - odd
        return min(odd, even)

# 134. Gas Station
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 
