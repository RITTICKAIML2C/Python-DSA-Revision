# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
class Solution:
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split()
        for i, word in enumerate(words, start=1):
            if word.startswith(searchWord):
                return i
        return -1

# 2110. Number of Smooth Descent Periods of a Stock
class Solution:
    def getDescentPeriods(self, prices):
        total = 0
        streak = 0
        for i in range(len(prices)):
            if i > 0 and prices[i] == prices[i - 1] - 1:
                streak += 1
            else:
                streak = 1
            total += streak
        return total


