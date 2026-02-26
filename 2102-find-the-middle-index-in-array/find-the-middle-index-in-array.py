class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n=len(nums)
        p=[0]*n
        p[0]=nums[0]
        ans=-1
        for i in range(1,n):
            p[i]=nums[i]+p[i-1]
        if p[0]-p[-1]==0:
            return 0
        for i in range(1,n):
            if p[-1]-p[i]==p[i-1]:
                return i
        return -1