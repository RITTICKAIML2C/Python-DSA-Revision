# 414. Third Maximum Number
# You are given an integer array nums.
class Solution:
    def thirdMax(self, nums):
        first = second = third = None
        for num in nums:
            if num in (first, second, third):
                continue
            if first is None or num > first:
                first, second, third = num, first, second
            elif second is None or num > second:
                second, third = num, second
            elif third is None or num > third:
                third = num
        return third if t

# 718. Maximum Length of Repeated Subarray
# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
class Solution:
    def findLength(self, nums1, nums2):
        m, n = len(nums1), len(nums2)

        dp = [0] * (n + 1)
        result = 0

        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                    result = max(result, dp[j])
                else:
                    dp[j] = 0

        return result
