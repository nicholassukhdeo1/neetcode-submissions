# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        merged_list = []

        temp = list1 # ur not given a list of nodes here. its just the first node of list1.
        temp2 = list2 

        while temp is not None:
            merged_list.append(temp.val)
            temp = temp.next

        while temp2 is not None:
            merged_list.append(temp2.val)
            temp2 = temp2.next

        if len(merged_list) == 0:
            return None

        merged_list.sort()

        dummy = ListNode(merged_list[0])
        current = dummy

        for index in range(1, len(merged_list)):
            current.next = ListNode(merged_list[index])
            current = current.next
           

        return dummy