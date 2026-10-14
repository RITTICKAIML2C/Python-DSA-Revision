# 628. Maximum Product of Three Numbers
# You are given an integer array nums.
class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1]
        )

# 162. Find Peak Element
# A peak element is an element that is strictly greater than its neighbors.
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
