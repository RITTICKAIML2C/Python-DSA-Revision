# 1876 
class Solution:
    def countGoodSubstrings(self, s):
        count = 0

        for i in range(len(s) - 2):
            window = s[i:i + 3]

            if len(set(window)) == 3:
                count += 1

        return count

# 904
class Solution:
    def totalFruit(self, fruits):
        basket = {}
        left = 0
        result = 0

        for right in range(len(fruits)):
            fruit = fruits[right]

            basket[fruit] = basket.get(fruit, 0) + 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                left += 1

            result = max(result, right - left + 1)

        return result
