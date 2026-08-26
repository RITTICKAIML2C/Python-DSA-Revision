# 129. Sum Root to Leaf Numbers
# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
class Solution:
    def sumNumbers(self, root):
        def dfs(node, number):
            if not node:
                return 0
            number = number * 10 + node.val
            if not node.left and not node.right:
                return number
            return (
                dfs(node.left, number)
                + dfs(node.right, number)
            )
        return dfs(root, 0)

# 110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            if abs(left - right) > 1:
                return -1
            if left == -1 or right == -1:
                return -1
            return 1 + max(left, right)
        return height(root) != -1
