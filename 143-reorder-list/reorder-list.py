# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        f=head.next
        slow=head
        while f and f.next:
            f=f.next.next
            slow=slow.next
        s=slow.next

        # reversing 
        p=slow.next=None
        while s:
            temp=s.next
            s.next=p
            p=s
            s=temp
        #reordering 
        crnt=head
        s=p
        while s:
            temp1,temp2=crnt.next,s.next
            crnt.next=s
            s.next=temp1
            crnt,s=temp1,temp2