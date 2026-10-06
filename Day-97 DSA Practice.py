# 771. Jewels and Stones
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
class Solution:
    def numJewelsInStones(self, jewels, stones):
        jewels = set(jewels)
        return sum(stone in jewels for stone in stones)

# 735. Asteroid Collision
# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.
class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            alive = True
            while alive and asteroid < 0 and stack and stack[-1] > 0:
                if stack[-1] < -asteroid:
                    stack.pop()
                elif stack[-1] == -asteroid:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(asteroid)
        return stack
