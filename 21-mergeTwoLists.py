# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# recursively solution
class Solution(object):
    # def mergeTwoLists(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     rtype: ListNode
    #     """
    #     if not l1 or not l2:
    #         return l1 or l2
    #     if l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l2.next, l1)
    #         return l2

    # iteratively
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
