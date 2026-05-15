class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        total=nums[0]
        for i in range(1,len(nums)):
            if i%2:
                total-=nums[i]
            else:
                total+=nums[i]
        return total