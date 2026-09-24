# 724. Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.
class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0
        for i, x in enumerate(nums):
            if left == total - left - x:
                return i
            left += x
        return -1

# 152. Maximum Product Subarray
# Given an integer array nums, find a subarray that has the largest product, and return the product.
# class Solution:
    def maxProduct(self, nums):
        cur_max = cur_min = ans = nums[0]
        for x in nums[1:]:
            if x < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(x, cur_max * x)
            cur_min = min(x, cur_min * x)
            ans = max(ans, cur_max)
        return ans
