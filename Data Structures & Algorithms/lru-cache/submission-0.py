class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dummy=Node()
        self.hashmap={}
        self.dummy.prev=self.dummy
        self.dummy.next=self.dummy

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def add(self,node):
        node.prev=self.dummy
        node.next=self.dummy.next
        node.prev.next=node
        node.next.prev=node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node=self.hashmap[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        node=Node(key,value)
        self.hashmap[key]=node
        self.add(node)
        if len(self.hashmap)>self.capacity:
            backnode=self.dummy.prev
            del self.hashmap[backnode.key]
            self.remove(backnode)

