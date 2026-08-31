# 438. Find All Anagrams in a String
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        need = Counter(p)
        window = Counter()
        result = []
        k = len(p)
        for i, ch in enumerate(s):
            window[ch] += 1
            if i >= k:
                old = s[i-k]
                window[old] -= 1
                if window[old] == 0:
                    del window[old]
            if window == need:
                result.append(i-k+1)
        return result

# 589. N-ary Tree Preorder Traversal
# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
class Solution:
    def preorder(self, root):
        result = []
        def dfs(node):
            if not node:
                return
            result.append(node.val)
            for child in node.children:
                dfs(child)
        dfs(root)
