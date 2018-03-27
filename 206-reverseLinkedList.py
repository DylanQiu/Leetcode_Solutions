class Solution(object):
    def reverseList(self, head):
        """
        reverse a singly linked list
        :param head: ListNode
        :return: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

