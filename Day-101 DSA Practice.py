# 367. Valid Perfect Square
# Given a positive integer num, return true if num is a perfect square or false otherwise.
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            if square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

# 767. Reorganize String
# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        if max(freq.values()) > (len(s) + 1) // 2:
            return ""
        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)
        result = []
        while len(heap) > 1:
            c1, a = heapq.heappop(heap)
            c2, b = heapq.heappop(heap)
            result.extend([a, b])
            if c1 < -1:
                heapq.heappush(heap, (c1 + 1, a))
            if c2 < -1:
                heapq.heappush(heap, (c2 + 1, b))
        if heap:
            result.append(heap[0][1])
        return "".join(result)
