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
            return
        hashmap={}
        cur=head
        while cur:
            hashmap[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            copy=hashmap[cur]
            copy.next=hashmap[cur.next] if cur.next else None
            copy.random=hashmap[cur.random] if cur.random else None
            cur=cur.next
        return hashmap[head]