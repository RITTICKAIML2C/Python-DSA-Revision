# 409. Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        count = Counter(s)
        length = 0
        odd = False
        for x in count.values():
            length += (x // 2) * 2
            if x % 2:
                odd = True
        return length + odd

# 452. Minimum Number of Arrows to Burst Balloons
# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend.
class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        for start, finish in points[1:]:
            if start > end:
                arrows += 1
                end = finish
        return arrows
