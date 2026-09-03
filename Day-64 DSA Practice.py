# 605. Can Place Flowers
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i - 1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            if flowerbed[i] == 0 and left and right:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False

# 881. Boats to Save People
# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats
