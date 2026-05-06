class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefixS=[0]
        x=len(nums)
        ans=[]
        for i in range(len(nums)):
            p=prefixS[-1]+nums[i]
            prefixS.append(p)
        for i,n in enumerate(nums):
            preSum=prefixS[i]
            postSum=prefixS[-1]-prefixS[i+1]
            a=((i*n)-preSum)+(postSum-n*(x-i-1))
            ans.append(a)
        return ans