# 617. Merge Two Binary Trees
# You are given two binary trees root1 and root2.
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(
            root1.left, root2.left
        )
        root1.right = self.mergeTrees(
            root1.right, root2.right
        )
        return root1

# 1022. Sum of Root To Leaf Binary Numbers
# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.
# The test cases are generated so that the answer fits in a 32-bits integer.
class Solution:
    def sumRootToLeaf(self, root):
        def dfs(node, value):
            if not node:
                return 0
            value = value * 2 + node.val
            if not node.left and not node.right:
                return value
            return (
                dfs(node.left, value)
                + dfs(node.right, value)
            )
        return dfs(root, 0)
