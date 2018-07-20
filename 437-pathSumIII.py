# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(node, sum):
            if not node:
                return 0
            return sum == node.val + dfs(node.left, sum-node.val) + dfs(node.right, sum-node.val)

        if not root:
            return 0
        return dfs(root, sum) + dfs(root.left, sum) + dfs(root.right, sum)