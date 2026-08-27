# 700. Search in a Binary Search Tree
# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
class Solution:
    def searchBST(self, root, val):
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)

# 1382. Balance a Binary Search Tree
# Given the root of a binary search tree, return a balanced binary search tree with the same node values. 
# If there is more than one answer, return any of them.
class Solution:
    def balanceBST(self, root):
        values = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node)
            inorder(node.right)
        inorder(root)
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = values[mid]
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node
        return build(0, len(values) - 1)
