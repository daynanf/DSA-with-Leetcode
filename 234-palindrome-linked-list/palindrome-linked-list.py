# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n=head
        arr=[]
        while n:
            arr.append(n.val)
            n=n.next
        r=len(arr)-1
        cnt=0
        for i in range(len(arr)//2):
            if arr[i]==arr[r]:
                cnt+=1
            r-=1
        return cnt==len(arr)//2