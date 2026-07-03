# Q : 1480. Running Sum of 1d Array
# Hint : Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums

# Q : 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
class Solution:
    def maxArea(self, height):
        maximum = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                width = j - i
                h = min(height[i], height[j])
                area = width * h
                if area > maximum:
                    maximum = area
        return maximum
