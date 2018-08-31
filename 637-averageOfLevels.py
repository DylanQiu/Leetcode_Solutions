# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            tmp = 0
            s = len(queue)
            curqueue = []
            for i in range(s):
                node = queue.pop()
                if node.left:
                    curqueue.append(node.left)
                if node.right:
                    curqueue.append(node.right)
                tmp += node.val
            ans.append(float(tmp)/s)
            queue = curqueue
        return ans