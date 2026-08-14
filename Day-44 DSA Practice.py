# 841. Keys and Rooms
# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
class Solution:
    def canVisitAllRooms(self, rooms):
        visited = set()
        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)
        dfs(0)
        return len(visited) == len(rooms)

# 684. Redundant Connection
# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed
class Solution:
    def findRedundantConnection(self, edges):
        parent = list(range(len(edges) + 1))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for a, b in edges:
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return [a, b]
            parent[pa] = pb
