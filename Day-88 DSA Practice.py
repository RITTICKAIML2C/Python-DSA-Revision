# 394. Decode String
# Given an encoded string, return its decoded string.
class Solution:
    def decodeString(self, s):
        stack = []
        num = 0
        cur = ""
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append((cur, num))
                cur = ""
                num = 0
            elif ch == ']':
                prev, repeat = stack.pop()
                cur = prev + cur * repeat
            else:
                cur += ch
        return cur

# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
class Solution:
    def productExceptSelf(self, nums):
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result


