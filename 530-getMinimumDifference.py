# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, l=[]):
            if node.left:
                dfs(node.left, l)
            l.append(node.val)
            if node.right:
                dfs(node.right, l)
            return l
        l = dfs(root)
        return min([abs(a-b) for a,b in zip(l, l[1:])])