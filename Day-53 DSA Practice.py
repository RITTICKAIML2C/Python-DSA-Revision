# 543. Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return diameter

# 450. Delete Node in a BST
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
# Return the root node reference (possibly updated) of the BST.
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(
                root.right,
                successor.val
            )
        return root
        
