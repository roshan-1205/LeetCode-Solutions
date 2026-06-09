"""Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed."""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            curr = prev.next
            tail = prev

            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            next_group = tail.next
            curr_node = curr
            prev_node = next_group

            for _ in range(k):
                temp = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = temp

            prev.next = tail
            prev = curr

        return dummy.next