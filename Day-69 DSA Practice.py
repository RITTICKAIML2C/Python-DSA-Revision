# 1351. Count Negative Numbers in a Sorted Matrix
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
class Solution:
    def countNegatives(self, grid):
        count = 0
        row = 0
        col = len(grid[0]) - 1
        while row < len(grid) and col >= 0:
            if grid[row][col] < 0:
                count += len(grid) - row
                col -= 1
            else:
                row += 1
        return count

# 1011. Capacity To Ship Packages Within D Days
# A conveyor belt has packages that must be shipped from one port to another within days days.
class Solution:
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)
        while left < right:
            capacity = (left + right) // 2
            needed_days = 1
            current = 0
            for weight in weights:
                if current + weight > capacity:
                    needed_days += 1
                    current = 0
                current += weight
            if needed_days <= days:
                right = capacity
            else:
                left = capacity + 1
        return left
