# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        cnt=1
        n=head
        prevAd=None
        startAd=None
        prev=None
        while n:
            temp=n.next
            if cnt==left-1:
                prevAd=n
            elif cnt==left:
                startAd=n
            if cnt>=left and cnt<=right:
                n.next=prev
                prev=n
                if cnt==right:
                    if prevAd:
                        prevAd.next=n
                    else:
                        head=n
            elif cnt==right+1:
                startAd.next=n
            n=temp
            cnt+=1
        return head