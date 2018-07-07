# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = head
        count = 0
        if n == 0:
            return head
        while l:
            count += 1
            l = l.next
        step = count-n
        if step == 0:
            return head.next
        l = head
        for i in xrange(1, step):
            l = l.next
        l.next = l.next.next
        return head