"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        if head is None:
            return
        copies = {}

        curr = head

        while curr:
            new_curr = Node(curr.val)
            copies[curr] = new_curr
            curr = curr.next

        curr = head

        while curr:
            new_curr = copies[curr]
            if curr.next is not None:
                new_curr.next = copies[curr.next]
            if curr.random is not None:
                new_curr.random = copies[curr.random]
            curr = curr.next


        return copies[head]
            