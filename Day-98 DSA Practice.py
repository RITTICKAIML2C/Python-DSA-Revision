# 766. Toeplitz Matrix
# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
class Solution:
    def isToeplitzMatrix(self, matrix):
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] != matrix[r-1][c-1]:
                    return False
        return True

# 918. Maximum Sum Circular Subarray
# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
class Solution:
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)
        cur_max = max_sum = nums[0]
        cur_min = min_sum = nums[0]
        for x in nums[1:]:
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)
            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)
