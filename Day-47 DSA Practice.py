# 875. Koko Eating Bananas
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Return the minimum integer k such that she can eat all the bananas within h hours.
class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left

# 374. Guess Number Higher or Lower
# I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
class Solution:
    def guessNumber(self, n):
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1
