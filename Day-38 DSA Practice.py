# 637. Average of Levels in Binary Tree
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
from collections import deque
class Solution:
    def averageOfLevels(self, root):
        q = deque([root])
        result = []
        while q:
            total = 0
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(total / size)
        return result

# 1091. Shortest Path in Binary Matrix
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        q = deque([(0, 0, 1)])
        grid[0][0] = 1
        directions = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),          (0,1),
            (1,-1),  (1,0),  (1,1)
        ]
        while q:
            r, c, distance = q.popleft()
            if r == n-1 and c == n-1:
                return distance
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < n and
                    0 <= nc < n and
                    grid[nr][nc] == 0):
                    grid[nr][nc] = 1
                    q.append((nr, nc, distance + 1))
        return -1
