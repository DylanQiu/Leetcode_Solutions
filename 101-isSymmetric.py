# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
        return p == q

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True
        cur1 = cur2 = root
        return self.isSameTree(cur1, cur2)

    def isSymmetric2(self, root):
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True
