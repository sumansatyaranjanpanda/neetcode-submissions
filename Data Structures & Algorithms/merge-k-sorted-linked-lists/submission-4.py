import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        heap=[]
        dummy=ListNode()
        curr=dummy

        # first head of all nodes pushed to mean heap in tuple formate in heap named list
        # heap=[(1,0,node(1)),(2,1,node(2))......]

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))

        
        while heap:
            val,i,node=heapq.heappop(heap)

            curr.next=node
            curr=node
            node=node.next

            if node:
                heapq.heappush(heap,(node.val,i,node))

        return dummy.next




        
