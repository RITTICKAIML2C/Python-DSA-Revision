# 496. Next Greater Element I
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        return [
            next_greater.get(num, -1)
            for num in nums1
        ]

# 853. Car Fleet
# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
# You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(
            zip(position, speed),
            reverse=True
        )
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
