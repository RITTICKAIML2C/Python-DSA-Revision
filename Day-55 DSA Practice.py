# 103. Binary Tree Zigzag Level Order Traversal
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
# (i.e., from left to right, then right to left for the next level and alternate between).
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        q = deque([root])
        result = []
        left_to_right = True
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not left_to_right:
                level.reverse()
            result.append(level)
            left_to_right = not left_to_right
        return result

# 107. Binary Tree Level Order Traversal II
# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
# (i.e., from left to right, level by level from leaf to root).
from collections import deque
class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result[::-1]
