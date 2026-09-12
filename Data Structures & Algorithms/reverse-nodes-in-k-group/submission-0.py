# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        cur=head
        while cur:
            cur=cur.next
            n+=1
        s=n//k
        dummy=ListNode(0,head)
        pre=dummy
        cur=head
        for _ in range(s):
            for _ in range(k-1):
                next=cur.next
                cur.next=next.next
                next.next=pre.next
                pre.next=next
            pre=cur
            cur=cur.next
        return dummy.next

        