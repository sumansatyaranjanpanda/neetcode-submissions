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



        if not head:
            return None


        curr=head

        while curr:
            copy=Node(curr.val)

            copy.next=curr.next
            curr.next=copy

            curr=curr.next.next

        curr=head

        while curr:
            if curr.random:
                curr.next.random=curr.random.next

            curr=curr.next.next


        curr=head
        copy_head=head.next


        while curr:
            copy=curr.next
            curr.next=copy.next

            if copy.next:
                copy.next=copy.next.next

            curr=curr.next

        return copy_head


        