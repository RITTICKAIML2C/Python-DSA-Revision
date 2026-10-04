# 713. Subarray Product Less Than K
# You are given an array of integers nums and an integer k.
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        left = 0
        product = 1
        ans = 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            ans += right - left + 1
        return ans

# 965. Univalued Binary Tree
# A binary tree is uni-valued if every node in the tree has the same value.
class Solution:
    def isUnivalTree(self, root):
        def dfs(node):
            if not node:
                return True
            if node.val != root.val:
                return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)
