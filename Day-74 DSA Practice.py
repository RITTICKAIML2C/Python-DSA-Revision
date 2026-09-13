# 415. Add Strings
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
class Solution:
    def addStrings(self, num1, num2):
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            total = a + b + carry
            result.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1
        return ''.join(result[::-1])

# 518. Coin Change II
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]
