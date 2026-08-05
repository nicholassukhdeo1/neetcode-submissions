class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        lead = head
        drag = None

        if head is None:
            return None

        while lead is not None:
            temp = lead.next
            lead.next = drag
            drag = lead
            lead = temp

        return drag