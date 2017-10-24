# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        cur = head
        # if not cur.next:
        #     return head
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

# a = ListNode(10)
# b = ListNode(9)
# c = ListNode(9)
# a.next = b
# print a.val
# b.next = c
#
# print a.val
# print a.next.val
# print a.next.next.val
# # print a.next.next.next.val
# sol = Solution()
# sol.deleteDuplicates([])
# Solution.deleteDuplicates(a)

# print a.val
# print a.next.val
# print a.next.next.val
