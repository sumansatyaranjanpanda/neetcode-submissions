class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.head=Node()
        self.tail=Node()

        self.head.next=self.tail
        self.tail.prev=self.head

    def _remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def add_on_head(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node

        

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node=self.cache[key]

        self._remove(node)
        self.add_on_head(node)

        return node.value




        

    def put(self, key: int, value: int) -> None:


        # if key is already available

        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            del self.cache[key]

        if len(self.cache)>=self.cap:
            node=self.tail.prev
            self._remove(node)
            del self.cache[node.key]

        node=Node(key,value)
        self.cache[key]=node
        self.add_on_head(node)
        
