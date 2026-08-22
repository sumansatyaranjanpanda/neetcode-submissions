# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        need=[]

        temp = head

        while temp !=None :

            if temp in need:
                return True


            need.append(temp)
            temp=temp.next


        return False
    

        