# 1021. Remove Outermost Parentheses
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
class Solution:
    def removeOuterParentheses(self, s):
        depth = 0
        result = []
        for ch in s:
            if ch == '(':
                if depth > 0:
                    result.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result.append(ch)
        return ''.join(result)

# 846. Hand of Straights
# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
from collections import Counter
class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for card in sorted(count):
            if count[card] > 0:
                needed = count[card]
                for x in range(card, card + groupSize):
                    if count[x] < needed:
                        return False
                    count[x] -= needed
        return True
