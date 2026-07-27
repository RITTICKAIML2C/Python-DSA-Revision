# 74. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
class Solution:
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid // cols][mid % cols]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

# 278. First Bad Version
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
