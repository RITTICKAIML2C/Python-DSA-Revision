# 145. Binary Tree Postorder Traversal
# Given the root of a binary tree, return the postorder traversal of its nodes' values.
class Solution:
    def postorderTraversal(self, root):
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
        dfs(root)
        return result

# 114. Flatten Binary Tree to Linked List
# Given the root of a binary tree, flatten the tree into a "linked list"
class Solution:
    def flatten(self, root):
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        right_subtree = root.right
        root.right = root.left
        root.left = None
        current = root
        while current.right:
            current = current.right
        current.right = right_subtree
