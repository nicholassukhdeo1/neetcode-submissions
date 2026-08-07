# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # get pointers into position (slow at middle)
        if not head or not head.next:
            return
        fast = head
        slow = head
        slow_prev = None

        while fast and fast.next:
            fast = fast.next.next
            slow_prev = slow
            slow = slow.next

        #split the list in half
        slow_prev.next = None
        l2 = slow
        prev_reverse = None

        #reverse the 2nd half
        while slow is not None:
            temp = slow.next
            slow.next = prev_reverse
            prev_reverse = slow
            slow = temp

        #merge the list
        l1 = head
        l2 = prev_reverse
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            if l1_next:
                l2.next = l1_next
            
            l1 = l1_next
            l2 = l2_next
            
