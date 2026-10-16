# 520. Detect Capital
# We define the usage of capitals in a word to be right when one of the following cases holds:
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (word.isupper() or word.islower()
                or word.istitle())

# 1838. Frequency of the Most Frequent Element
# The frequency of an element is the number of times it occurs in an array.
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = total = ans = 0
        for right, x in enumerate(nums):
            total += x
            while x * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
      
