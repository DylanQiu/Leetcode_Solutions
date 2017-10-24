# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        centre = len(nums) / 2
        root = TreeNode(nums[centre])
        root.left = self.sortedArrayToBST(nums[:centre])
        root.right = self.sortedArrayToBST(nums[centre+1:])

        return root
