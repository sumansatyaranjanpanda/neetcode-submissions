# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast=head
        slow=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        
        head1=slow.next
        slow.next=None

        prev=None


        while head1!=None:
            temp=head1.next
            head1.next=prev
            prev=head1
            head1=temp

        second=head1=prev

        first=head

        while second:

            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2

        










