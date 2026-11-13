# 1200. Minimum Absolute Difference
# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = float('inf')
        # Find minimum difference
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            min_diff = min(min_diff, diff)
        result = []
        # Collect all pairs with minimum difference
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])
        return result

# 801. Minimum Swaps To Make Sequences Increasing
# You are given two integer arrays of the same length nums1 and nums2. In one operation, you are allowed to swap nums1[i] with nums2[i].
class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        # Base cases at index 0
        # keep[0]: 0 swaps if we don't swap at index 0
        # swap[0]: 1 swap if we swap at index 0
        keep, swap = 0, 1
        
        for i in range(1, n):
            # Initialize with infinity
            nxt_keep = float('inf')
            nxt_swap = float('inf')
            
            # Condition A: Natural order holds (no new cross-sw swaps required)
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                nxt_keep = min(nxt_keep, keep)
                nxt_swap = min(nxt_swap, swap + 1)
                
            # Condition B: Cross order holds (swapping at i-1 or i fixes the order)
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                nxt_keep = min(nxt_keep, swap)
                nxt_swap = min(nxt_swap, keep + 1)
                
            keep, swap = nxt_keep, nxt_swap
            
        return min(keep, swap)
