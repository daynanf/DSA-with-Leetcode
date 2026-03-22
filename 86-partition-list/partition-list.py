# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr=[]
        n=head
        while n:
            arr.append(n.val)
            n=n.next
        target=ListNode(x)
        t=target
        next=target.next
        before=ListNode(0)
        b=before
        for num in arr:
            if num<x:
                newNode=ListNode(num)
                before.next=newNode
                before=before.next
            else:
                newNode=ListNode(num)
                target.next=newNode
                target=target.next
        before.next=t.next
        return b.next