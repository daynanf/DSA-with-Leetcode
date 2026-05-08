class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddIndx=[]
        ans=0
        for i,x in enumerate(nums):
            if x%2:
                oddIndx.append(i)
        for i in range(len(oddIndx)-k+1):
            evenL=0
            if i==0:
                evenL=oddIndx[i]
            else:
                evenL=oddIndx[i]-oddIndx[i-1]-1
            evenR=0
            if oddIndx[i+k-1]==oddIndx[-1]:
                evenR=len(nums)-oddIndx[i+k-1]-1
            else:
                evenR=oddIndx[i+k]-oddIndx[i+k-1]-1
            ans+=(evenR+1)*(evenL+1) # if evenL>0 or evenR>0 else 1
        return ans