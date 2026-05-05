class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq=dict()
        ans=[]
        for x in nums:
            freq[x]=freq.get(x,0)+1
            if freq[x]==2:
                ans.append(x)
        return ans
