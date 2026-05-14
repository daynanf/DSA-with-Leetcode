class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=max(nums)
        if nums.count(n)==2 and len(set(nums))==n and len(nums)==n+1:
            return True
        else:
            return False