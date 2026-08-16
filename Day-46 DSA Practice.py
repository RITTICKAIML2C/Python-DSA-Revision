# 705. Design HashSet
# Design a HashSet without using any built-in hash table libraries.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
class MyHashSet:
    def __init__(self):
        self.data = [False] * 1000001
    def add(self, key):
        self.data[key] = True
    def remove(self, key):
        self.data[key] = False
    def contains(self, key):
        return self.data[key]

# 787. Cheapest Flights Within K Stops
# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k + 1):
            temp = prices.copy()
            for u, v, price in flights:
                if prices[u] != float("inf"):
                    temp[v] = min(
                        temp[v],
                        prices[u] + price
                    )
            prices = temp
        return prices[dst] if prices[dst] != float("inf") else -1
