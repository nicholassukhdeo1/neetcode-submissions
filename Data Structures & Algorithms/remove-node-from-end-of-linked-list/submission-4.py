# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        dummy = ListNode()
        prev = dummy
        dummy.next = head

        if head is None:
            return

        
        R = head


        for iteration in range(n):
            R = R.next

        while R is not None:
            prev = prev.next
            R = R.next

        prev.next = prev.next.next

        return dummy.next