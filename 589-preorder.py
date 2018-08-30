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
    # def preorder(self, root):
    #     """
    #     :type root: Node
    #     :rtype: List[int]
    #     """
    #
    #     if not root:
    #         return []
    #     self.ans.append(root.val)
    #     for child in root.children:
    #         self.preorder(child)
    #     return self.ans

    def preorder(self, root):
        stack = []
        ans = []
        if not root:
            return []
        stack.append(root)
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend([child for child in node.children[::-1] if child])
        return ans