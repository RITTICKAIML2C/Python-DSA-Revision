# 594. Longest Harmonious Subsequence
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
from collections import Counter
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        freq = Counter(nums)
        ans = 0
        for x in freq:
            if x + 1 in freq:
                ans = max(ans, freq[x] + freq[x + 1])
        return ans

# 986. Interval List Intersections
# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
class Solution:
    def intervalIntersection(self, firstList, secondList):
        i = j = 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                ans.append([start, end])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans
      
