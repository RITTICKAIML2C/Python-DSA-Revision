# 743 — Network Delay Time
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        heap = [(0, k)]
        dist = {}
        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = time
            for nei, weight in graph[node]:
                heapq.heappush(
                    heap,
                    (time + weight, nei)
                )
        if len(dist) != n:
            return -1
        return max(dist.values())
      
# 695. Max Area of Island
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
class Solution:
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )
        answer = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    answer = max(answer, dfs(r, c))
        return answer
