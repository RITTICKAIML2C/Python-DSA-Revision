# 997. Find the Town Judge
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
class Solution:
    def findJudge(self, n, trust):
        score = [0] * (n + 1)
        for a, b in trust:
            score[a] -= 1
            score[b] += 1
        for person in range(1, n + 1):
            if score[person] == n - 1:
                return person
        return -1

# 785. Is Graph Bipartite?
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.
# Return true if and only if it is bipartite.
from collections import deque
class Solution:
    def isBipartite(self, graph):
        color = {}
        for start in range(len(graph)):
            if start in color:
                continue
            color[start] = 0
            q = deque([start])
            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]
                        q.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
        return True
