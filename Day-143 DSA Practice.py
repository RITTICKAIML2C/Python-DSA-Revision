# 883. Projection Area of 3D Shapes
class Solution:
    def projectionArea(self, grid):
        n = len(grid)
        top = 0
        front = 0
        side = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    top += 1
            front += max(grid[i])
            side += max(grid[j][i] for j in range(n))
        return top + front + side

# 1014. Best Sightseeing Pair
class Solution:
    def maxScoreSightseeingPair(self, values):
        best_left = values[0]
        result = 0
        for j in range(1, len(values)):
            result = max(
                result,
                best_left + values[j] - j
            )
            best_left = max(
                best_left,
                values[j] + j
            )
        return result
