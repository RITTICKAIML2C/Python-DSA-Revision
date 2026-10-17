# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# You are given an array of integers nums and an integer limit.
from collections import deque
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        maxq, minq = deque(), deque()
        left = ans = 0
        for right, x in enumerate(nums):
            while maxq and nums[maxq[-1]] < x:
                maxq.pop()
            maxq.append(right)
            while minq and nums[minq[-1]] > x:
                minq.pop()
            minq.append(right)
            while nums[maxq[0]] - nums[minq[0]] > limit:
                left += 1
                if maxq[0] < left:
                    maxq.popleft()
                if minq[0] < left:
                    minq.popleft()
            ans = max(ans, right - left + 1)
        return ans
