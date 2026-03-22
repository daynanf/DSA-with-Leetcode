# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        if not head or not head.next:
            return None
        fast=dummy.next
        slow=dummy
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next