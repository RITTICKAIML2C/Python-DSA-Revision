# 797. All Paths From Source to Target
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
class Solution:
    def allPathsSourceTarget(self, graph):
        result = []
        def dfs(node, path):
            if node == len(graph) - 1:
                result.append(path[:])
                return
            for nxt in graph[node]:
                dfs(nxt, path + [nxt])
        dfs(0, [0])
        return result

# 491. Non-decreasing Subsequences
# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.
class Solution:
    def findSubsequences(self, nums):
        result = []
        def backtrack(start, path):
            if len(path) >= 2:
                result.append(path[:])
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                if path and nums[i] < path[-1]:
                    continue
                used.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return result 
