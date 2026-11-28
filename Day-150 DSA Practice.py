# 1464. Maximum Product of Two Elements in an Array
class Solution:
    def maxProduct(self, nums):
        first = second = 0
        for num in nums:
            if num >= first:
                second = first
                first = num
            elif num > second:
                second = num
        return (first - 1) * (second - 1)

# 2131. Longest Palindrome by Concatenating Two Letter Words
from collections import Counter
class Solution:
    def longestPalindrome(self, words):
        freq = Counter(words)
        length = 0
        center_used = False
        for word in list(freq.keys()):
            reverse = word[::-1]
            if word == reverse:
                pairs = freq[word] // 2
                length += pairs * 4
                if freq[word] % 2 == 1:
                    center_used = True
                freq[word] = 0
            elif word < reverse:
                pairs = min(freq[word], freq[reverse])
                length += pairs * 4
                freq[word] = 0
                freq[reverse] = 0
        if center_used:
            length += 2
        return length

