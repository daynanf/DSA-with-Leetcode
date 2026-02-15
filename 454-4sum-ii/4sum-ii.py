class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        countAB = defaultdict(int)
        for a in nums1:
            for b in nums2:
                countAB[a + b] += 1
        ans = 0
        for c in nums3:
            for d in nums4:
                ans += countAB[-(c + d)]
        return ans
