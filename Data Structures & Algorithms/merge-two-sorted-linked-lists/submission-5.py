# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        l1 = list1
        l2 = list2

        head = ListNode()
        memory = head

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            elif l2.val < l1.val:
                head.next = ListNode(l2.val)
                l2 = l2.next
            elif l1.val == l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            
            head = head.next

            

        
        while l1 is not None:
            head.next = ListNode(l1.val)
            l1 = l1.next
            head = head.next

        while l2 is not None:
            head.next = ListNode(l2.val)
            l2 = l2.next
            head = head.next

        
        return memory.next
            
        