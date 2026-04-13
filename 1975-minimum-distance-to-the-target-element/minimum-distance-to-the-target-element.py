class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        r=start
        l=start-1 if start>0 else 0
        ans=len(nums)
        while l>=0 or r<len(nums):
            left=len(nums)
            right=len(nums)
            if l>=0 and nums[l]==target:
                left=abs(l-start)
            if r<len(nums) and nums[r]==target:
               right=abs(r-start)
            ans=min(left,right,ans)
            l-=1
            r+=1
        return ans