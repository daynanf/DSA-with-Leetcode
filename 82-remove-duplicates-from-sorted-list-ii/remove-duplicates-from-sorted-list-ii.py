# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        dummy=ListNode()
        dummy.next=head
        crnt=head
        prev=dummy
        while crnt:
            if crnt.next and crnt.val==crnt.next.val:
                while crnt.next and crnt.val==crnt.next.val:
                    crnt=crnt.next
                prev.next=crnt.next
            else:
                prev=prev.next
            crnt=crnt.next
        return dummy.next
        