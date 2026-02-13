class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=len(nums1)
        n2=len(nums2)
        ans=[]
        it=list(set(nums1) & set(nums2))
        freq1=dict()
        for x in nums1:
            freq1[x]=freq1.get(x,0)+1
        freq2=dict()
        for x in nums2:
            freq2[x]=freq2.get(x,0)+1
        if n1<=n2: 
            for x in it:
                for _ in range(min(freq1[x],freq2[x])):
                    ans.append(x)
        else:
            for x in it:
                for _ in range(min(freq1[x],freq2[x])):
                    ans.append(x)
        return ans