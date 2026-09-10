# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur=head
        k=0
        while cur:
            cur=cur.next
            k+=1
        dummy=ListNode(0,head)
        cur=dummy
        for _ in range(k-n):
            cur=cur.next

        cur.next=cur.next.next
        return dummy.next