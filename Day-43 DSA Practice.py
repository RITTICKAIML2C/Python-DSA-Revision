# 547. Number of Provinces
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = set()
        provinces = 0
        def dfs(city):
            visited.add(city)
            for nei in range(n):
                if isConnected[city][nei] == 1 and nei not in visited:
                    dfs(nei)
        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)
        return provinces

# 130. Surrounded Regions
# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
class Solution:
    def solve(self, board):
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if board[r][c] != "O":
                return
            board[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        # Mark border-connected O's
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        # Capture surrounded O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
