# 1046. Last Stone Weight
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# Return the weight of the last remaining stone. If there are no stones left, return 0.
import heapq
class Solution:
    def lastStoneWeight(self, stones):
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, -(a - b))
        return -stones[0] if stones else 0

# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
