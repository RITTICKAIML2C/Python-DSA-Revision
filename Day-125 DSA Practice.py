# 523. Continuous Subarray Sum
# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
class Solution:
    def checkSubarraySum(self, nums, k):
        seen = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            rem = total % k
            if rem in seen:
                if i - seen[rem] >= 2:
                    return True
            else:
                seen[rem] = i
        return False

# 989. Add to Array-Form of Integer
# The array-form of an integer num is an array representing its digits in left to right order.
class Solution:
    def addToArrayForm(self, num, k):
        i = len(num) - 1
        while k > 0 and i >= 0:
            k += num[i]
            num[i] = k % 10
            k //= 10
            i -= 1
        while k > 0:
            num.insert(0, k % 10)
            k //= 10
        return num
