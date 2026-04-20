class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans=-1
        mini=nums[0]
        for i in range(len(nums)):
            if nums[i]>mini:
                ans=max(ans,nums[i]-mini)
            else:
                mini=nums[i]
        return ans 