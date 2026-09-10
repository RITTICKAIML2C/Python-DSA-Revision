# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.
class Solution:
    def reverseVowels(self, s):
        s = list(s)
        vowels = set("aeiouAEIOU")
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)

# 454. 4Sum II
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

from collections import Counter
class Solution:
    def fourSumCount(self, A, B, C, D):
        sums = Counter()
        for a in A:
            for b in B:
                sums[a + b] += 1
        count = 0
        for c in C:
            for d in D:
                count += sums[-(c + d)]
        return count
