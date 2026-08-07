# 542. 01 Matrix
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two cells sharing a common edge is 1.
from collections import deque
class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    mat[nr][nc] == -1):
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))
        return mat

# 1122. Relative Sort Array
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
class Solution:
    def relativeSortArray(self, arr1, arr2):
        order = {num: i for i, num in enumerate(arr2)}
        arr1.sort(key=lambda x: (order.get(x, len(arr2)), x))
        return arr1
