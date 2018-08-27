# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxD = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxDep(node):
            if not node:
                return 0
            l = maxDep(node.left)
            r = maxDep(node.right)
            self.maxD = max(l+r, self.maxD)
            return max(l, r)+1
        maxDep(root)
        return self.maxD