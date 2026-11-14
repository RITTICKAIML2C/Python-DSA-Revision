# Leetcode questions 1189
class Solution:
    def maxNumberOfBalloons(self, text):
        count = {}

        for char in text:
            count[char] = count.get(char, 0) + 1

        return min(
            count.get('b', 0),
            count.get('a', 0),
            count.get('l', 0) // 2,
            count.get('o', 0) // 2,
            count.get('n', 0)
        )

# Leetcode question 1493
class Solution:
    def longestSubarray(self, nums):
        left = 0
        zeros = 0
        result = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            result = max(result, right - left)

        return result
