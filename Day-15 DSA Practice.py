# 226. Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.
# Input: root = [4,2,7,1,3,6,9], Output: [4,7,2,9,6,3,1]
class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# Input: root = [2,1,3], Output: true
class Solution:
    def isValidBST(self, root):
        def check(node, minimum, maximum):
            if node is None:
                return True
            if node.val <= minimum or node.val >= maximum:
                return False
            return (
                check(node.left, minimum, node.val) and
                check(node.right, node.val, maximum)
            )
        return check(root, float("-inf"), float("inf"))
