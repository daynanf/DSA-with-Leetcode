class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq={0:1}
        curSum=0
        ans=0
        for i in range(len(nums)):
            curSum+=nums[i]
            ans+=freq.get(curSum%k,0)
            freq[curSum%k]=freq.get(curSum%k,0)+1
        return ans 