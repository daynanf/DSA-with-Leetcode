# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy=ListNode()
        dummy.next=head
        n=dummy
        while n and n.next:
            while n.next and n.next.val==val:
                n.next=n.next.next
            n=n.next
        return dummy.next