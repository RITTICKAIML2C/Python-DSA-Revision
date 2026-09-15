# 124. Binary Tree Maximum Path Sum
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
class Solution:
    def maxPathSum(self, root):
        self.answer = float("-inf")
        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.answer = max(
                self.answer,
                node.val + left + right
            )
            return node.val + max(left, right)
        dfs(root)
        return self.answer

# 228. Summary Ranges
# You are given a sorted unique integer array nums.
class Solution:
    def summaryRanges(self, nums):
        result = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            if start == nums[i]:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[i]}")
            i += 1
        return result
