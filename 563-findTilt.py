# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tile = 0
        if not root:
            return 0
        # self.tile += abs(self.findTilt(root.left) - self.findTilt(root.right))
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            self.tile += abs(left - right)
            return node.val + left + right
        dfs(root)
        return self.tile