# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast = head
        slow = head
        index = 0

        while slow is not None:

            if fast is None:
                return False
            if fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False
