# 101. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
class Solution:
    def isSymmetric(self, root):
        def check(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return (
                a.val == b.val
                and check(a.left, b.right)
                and check(a.right, b.left)
            )
        return check(root.left, root.right)

# 199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
from collections import deque
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
      
