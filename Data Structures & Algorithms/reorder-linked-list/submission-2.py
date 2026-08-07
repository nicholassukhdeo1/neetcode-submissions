# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # edge case
        if head is None or head.next is None:
            return


        # find middle point
        slow = head
        b4_slow = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            b4_slow = slow
            slow = slow.next

        # split the lists
        b4_slow.next = None
        l2 = slow
        l2_prev = None

        # reverse 2nd half of list
        while l2:
            temp = l2.next
            l2.next = l2_prev
            l2_prev = l2
            l2 = temp

        # then merge both lists
        l1 = head
        l2 = l2_prev
        while l1 and l2:
            # make temp ptrs first
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2

            if l1_next: #if it exists
                l2.next = l1_next

            l1 = l1_next
            l2 = l2_next
        