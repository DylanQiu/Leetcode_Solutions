"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    # def __init__(self):
    #     self.ans = []
    # def postorder(self, root):
    #     """
    #     :type root: Node
    #     :rtype: List[int]
    #     """
    #
    #     if not root:
    #         return []
    #     for child in root.children:
    #         self.postorder(child)
    #     self.ans.append(root.val)
    #     return self.ans

    def postorder(self, root):
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop(-1)
            ans.append(node.val)
            stack.extend(node.children)
        return ans[::-1]