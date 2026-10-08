# 1004. Max Consecutive Ones III
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = zeros = ans = 0
        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

# 171. Excel Sheet Column Number
# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result = result * 26 + ord(ch) - ord('A') + 1
        return result

  
