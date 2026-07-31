# 1337. The K Weakest Rows in a Matrix
# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). 
# The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
import heapq
class Solution:
    def kWeakestRows(self, mat, k):
        heap = []
        for i, row in enumerate(mat):
            soldiers = sum(row)
            heapq.heappush(heap, (soldiers, i))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

# 378. Kth Smallest Element in a Sorted Matrix
# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        heap = []
        for row in matrix:
            for num in row:
                heapq.heappush(heap, num)
        for _ in range(k - 1):
            heapq.heappop(heap)
        return heapq.heappop(heap)
