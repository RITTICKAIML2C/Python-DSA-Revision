# 1009. Complement of Base 10 Integer
# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
class Solution:
    def bitwiseComplement(self, n):
        if n == 0:
            return 1
        mask = (1 << n.bit_length()) - 1
        return n ^ mask

# 334. Increasing Triplet Subsequence
# Return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
class Solution:
    def increasingTriplet(self, nums):
        first = second = float("inf")
        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True
        return False
 
