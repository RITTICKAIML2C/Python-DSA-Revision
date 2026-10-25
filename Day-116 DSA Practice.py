# 557. Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
class Solution:
    def reverseWords(self, s):
        return " ".join(word[::-1] for word in s.split(" "))


# 91. Decode Ways
# You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:
class Solution:
    def numDecodings(self, s):
        if not s or s[0] == "0":
            return 0
        prev2, prev1 = 1, 1
        for i in range(1, len(s)):
            curr = 0
            if s[i] != "0":
                curr += prev1
            if 10 <= int(s[i-1:i+1]) <= 26:
                curr += prev2
            prev2, prev1 = prev1, curr
        return prev1
      
