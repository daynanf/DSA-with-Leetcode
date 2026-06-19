class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre=[0]
        for i in range(1,len(gain)+1):
            pre.append(pre[i-1]+gain[i-1])

        return max(pre)