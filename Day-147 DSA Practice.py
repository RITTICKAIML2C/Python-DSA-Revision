# 2134. Minimum Swaps to Group All 1's Together II
class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        ones = sum(nums)
        if ones <= 1:
            return 0
        # Count zeros in the first window
        zeros = ones - sum(nums[:ones])
        min_zeros = zeros

        # Slide the circular window
        for i in range(ones, n + ones):
            zeros += 1 - nums[i % n]
            zeros -= 1 - nums[(i - ones) % n]
            min_zeros = min(min_zeros, zeros)
        return min_zeros

# 1299. Replace Elements with Greatest Element on Right Side
class Solution:
    def replaceElements(self, arr):
        greatest = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = greatest
            greatest = max(greatest, current)
        return arr
