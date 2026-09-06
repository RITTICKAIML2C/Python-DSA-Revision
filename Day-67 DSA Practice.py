# 349. Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

# 611. Valid Triangle Number
# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        count = 0
        for k in range(len(nums) - 1, 1, -1):
            left = 0
            right = k - 1
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
