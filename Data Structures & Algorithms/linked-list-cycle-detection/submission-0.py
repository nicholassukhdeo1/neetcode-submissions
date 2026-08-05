# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head

        have_seen = defaultdict(int)

        while temp is not None:
            if have_seen[temp]:
                return True
            have_seen[temp] = 1
            temp = temp.next

        return False