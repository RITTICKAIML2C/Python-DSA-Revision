# 1365. How Many Numbers Are Smaller Than the Current Number
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        rank = {}
        for i, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = i
        return [rank[num] for num in nums]

# 974. Subarray Sums Divisible by K
# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
class Solution:
    def subarraysDivByK(self, nums, k):
        remainder_count = {0: 1}
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder in remainder_count:
                count += remainder_count[remainder]
            remainder_count[remainder] = (
                remainder_count.get(remainder, 0) + 1
            )
        return count



