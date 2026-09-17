# 205. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
class Solution:
    def isIsomorphic(self, s, t):
        a, b = {}, {}
        for x, y in zip(s, t):
            if (x in a and a[x] != y) or (y in b and b[y] != x):
                return False
            a[x] = y
            b[y] = x
        return True

# 424. Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
class Solution:
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        max_freq = 0
        ans = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
