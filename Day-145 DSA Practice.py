# 1433. Check If a String Can Break Another String
class Solution:
    def checkIfCanBreak(self, s1, s2):
        a = sorted(s1)
        b = sorted(s2)
        first = all(x >= y for x, y in zip(a, b))
        second = all(y >= x for x, y in zip(a, b))
        return first or second

# 1653. Minimum Deletions to Make String Balanced
class Solution:
    def minimumDeletions(self, s):
        b_count = 0
        deletions = 0
        for char in s:
            if char == 'b':
                b_count += 1
            else:
                deletions = min(
                    deletions + 1,
                    b_count
                )
        return deletions
      
