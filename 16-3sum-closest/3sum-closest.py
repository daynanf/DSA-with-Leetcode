class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=10**5
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and nums[i-1]==a:
                continue
            l,r=i+1,len(nums)-1
            while(l<r):
                threeSum=a+nums[l]+nums[r]
                ans= threeSum if abs(target-ans)>abs(target-threeSum) else ans
                if threeSum>target:
                    r-=1
                elif threeSum<target:
                    l+=1
                else:
                    return ans
        return ans
