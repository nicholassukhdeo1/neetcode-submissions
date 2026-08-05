# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        drag = None
        lead = head

        if head is None:
            return None
        elif head.next is None:
            return head

        while lead is not None:
            temp = lead.next
            lead.next = drag
            drag = lead
            lead = temp

        return drag