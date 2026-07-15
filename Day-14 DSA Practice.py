# 104. Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

# 102. Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from collections import deque
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        answer = []
        queue = deque([root])
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answer.append(level)
        return answer
