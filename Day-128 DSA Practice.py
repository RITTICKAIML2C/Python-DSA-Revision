# 1160. Find Words That Can Be Formed by Characters
# You are given an array of strings words and a string chars.
from collections import Counter
class Solution:
    def countCharacters(self, words, chars):
        available = Counter(chars)
        total = 0
        for word in words:
            needed = Counter(word)
            if all(needed[c] <= available[c] for c in needed):
                total += len(word)
        return total

# 1347. Minimum Number of Steps to Make Two Strings Anagram
# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
from collections import Counter
class Solution:
    def minSteps(self, s, t):
        a = Counter(s)
        b = Counter(t)
        return sum(max(0, a[c] - b[c]) for c in a)
      
