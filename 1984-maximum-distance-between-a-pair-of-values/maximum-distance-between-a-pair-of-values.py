class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans=j=0
        for i in range(len(nums1)):
            while j<len(nums2) and nums2[j]>=nums1[i]:
                ans=max(ans,j-i)
                j+=1
        return ans