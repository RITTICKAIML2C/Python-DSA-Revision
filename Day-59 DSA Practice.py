# 1306. Jump Game III
# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.
# Notice that you can not jump outside of the array at any time
class Solution:
    def canReach(self, arr, start):
        visited = set()
        def dfs(i):
            if i < 0 or i >= len(arr) or i in visited:
                return False
            if arr[i] == 0:
                return True
            visited.add(i)
            return dfs(i + arr[i]) or dfs(i - arr[i])
        return dfs(start)

# 399. Evaluate Division
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))
        def dfs(node, target, visited):
            if node == target:
                return 1.0
            visited.add(node)
            for nxt, weight in graph[node]:
                if nxt not in visited:
                    result = dfs(nxt, target, visited)
                    if result != -1:
                        return weight * result
            return -1.0
        answer = []
        for a, b in queries:
            if a not in graph or b not in graph:
                answer.append(-1.0)
            else:
                answer.append(dfs(a, b, set()))
        return answer
