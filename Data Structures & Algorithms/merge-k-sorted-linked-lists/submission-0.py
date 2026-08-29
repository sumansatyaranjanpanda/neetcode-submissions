import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        min_heap = []

        # Put first node of every list into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)

            # Add smallest node to result
            curr.next = node
            curr = curr.next

            # Add next node from same list
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next