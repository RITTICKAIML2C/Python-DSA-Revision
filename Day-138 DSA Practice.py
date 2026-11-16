# 350
from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        freq = Counter(nums1)
        result = []

        for num in nums2:
            if freq[num] > 0:
                result.append(num)
                freq[num] -= 1

        return result


# 825 
class Solution:
    def numFriendRequests(self, ages):
        count = [0] * 121

        for age in ages:
            count[age] += 1

        result = 0

        for age in range(15, 121):
            if count[age] == 0:
                continue

            for other in range(15, age + 1):
                if other <= 0.5 * age + 7:
                    continue

                result += count[age] * count[other]

                if age == other:
                    result -= count[age]

        return result
