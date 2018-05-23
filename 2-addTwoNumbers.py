# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def printl(self):
        print self.val
        if self.next:
            print self.next.val


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = l1
        while l1 and l2:
            l1.val = l1.val + l2.val
            if l1.val >= 10:
                l1.val -= 10
                if l1.next:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1)
            l2 = l2.next
            if l1.next is None:
                l1.next = l2
                break
            l1 = l1.next

        while l1.val >= 10:
            if l1.next:
                l1.next.val += 1
            else:
                l1.next = ListNode(1)
            l1.val -= 10
            l1 = l1.next

        return n

a = ListNode(0)
b = ListNode(7)
b.next = ListNode(3)
c = Solution()
d = c.addTwoNumbers(a, b)
d.printl()
print divmod(111,10)

