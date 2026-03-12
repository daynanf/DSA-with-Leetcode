# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        crnt=head.next
        prev=head
        while crnt:
            if prev.val==crnt.val:
                prev.next=crnt.next
            else:
                prev=crnt
            crnt=crnt.next
        return head