# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        def isMatch(s, t):
            if not (s and t):
                return s is t
            return (s.val == t.val) and isMatch(s.left, t.left) and isMatch(s.right, t.right)

        if isMatch(s,t):
            return True
        return self.isSubtree(s.left. t) or self.isSubtree(s.right, t)