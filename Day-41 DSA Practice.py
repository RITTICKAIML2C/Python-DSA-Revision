# 572. Subtree of Another Tree
# Given the roots of two binary trees root and subRoot, 
# return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
class Solution:
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        if self.same(root, subRoot):
            return True
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
    def same(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return (
            a.val == b.val
            and self.same(a.left, b.left)
            and self.same(a.right, b.right)
        )

# 1448. Count Good Nodes in Binary Tree
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.
class Solution:
    def goodNodes(self, root):
        def dfs(node, maximum):
            if not node:
                return 0
            good = 0
            if node.val >= maximum:
                good = 1
                maximum = node.val
            return (
                good
                + dfs(node.left, maximum)
                + dfs(node.right, maximum)
            )
        return dfs(root, root.val)
