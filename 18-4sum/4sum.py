class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and nums[i-1]==a:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j-1]==nums[j]:
                    continue
                l,r=j+1,len(nums)-1
                while(l<r):
                    fourSum=a+nums[l]+nums[r]+nums[j]
                    if fourSum>target:
                        r-=1
                    elif fourSum<target:
                        l+=1
                    else:
                        ans.append([a,nums[l],nums[r],nums[j]])
                        l+=1
                        while nums[l]==nums[l-1] and l<r :
                            l+=1
        return ans