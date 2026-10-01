# 796. Rotate String
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
class Solution:
    def rotateString(self, s, goal):
        return len(s) == len(goal) and goal in (s + s)

# 658. Find K Closest Elements
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
class Solution:
    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
