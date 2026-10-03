# 888. Fair Candy Swap
# Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number of candies of the ith box of candy that Alice has and bobSizes[j] is the number of candies of the jth box of candy that Bob has.
class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        bob = set(bobSizes)
        for a in aliceSizes:
            if a - diff in bob:
                return [a, a - diff]

# 417. Pacific Atlantic Water Flow
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
class Solution:
    def pacificAtlantic(self, heights):
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        return [list(cell) for cell in pacific & atlantic]
