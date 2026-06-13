"""Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)"""

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            a.next = b.next
            b.next = a
            prev.next = b
            prev = a

        return dummy.next