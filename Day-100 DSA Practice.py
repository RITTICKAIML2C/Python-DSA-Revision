# 202. Happy Number
# Write an algorithm to determine if a number n is happy.
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1   

# 647. Palindromic Substrings
# Given a string s, return the number of palindromic substrings in it.
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for left, right in ((i, i), (i, i + 1)):
                while (left >= 0 and right < len(s)
                       and s[left] == s[right]):
                    count += 1
                    left -= 1
                    right += 1
        return count
