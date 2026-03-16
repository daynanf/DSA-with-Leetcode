# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        la=0
        lb=0
        l1=headA
        l2=headB
        while l1:
            l1=l1.next
            la+=1
        while l2:
            l2=l2.next
            lb+=1
        l1=headA
        l2=headB
        for _ in range(abs(la-lb)):
            if la>lb:
                l1=l1.next
            elif la<lb:
                l2=l2.next
        while l1 and l2:
            if l1==l2:
                return l1
            l1=l1.next
            l2=l2.next
        return None