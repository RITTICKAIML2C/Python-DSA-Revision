# 733. Flood Fill
# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].
class Solution:
    def floodFill(self, image, sr, sc, color):
        original = image[sr][sc]
        if original == color:
            return image
        def dfs(r, c):
            if (
                r < 0 or
                r >= len(image) or
                c < 0 or
                c >= len(image[0]) or
                image[r][c] != original
            ):
                return
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        dfs(sr, sc)
        return image

# 200. Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        def dfs(r, c):
            if (
                r < 0 or
                r >= rows or
                c < 0 or
                c >= cols or
                grid[r][c] == "0"
            ):
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands
