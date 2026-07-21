class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        if s.count("0") <= 1 or s.count("1") < 1 :
            return s.count("1")
        zeroArr=[] 
        zeroArr=[len(run) for run in s.split('1') if run]
        if len(zeroArr) < 2:
            return s.count("1") 
        ans=[]
        for i,x in enumerate(zeroArr):
            if i<len(zeroArr)-1:
                ans.append(x + zeroArr[i+1])
            else:
                ans.append(x)
        return max(ans) + s.count("1")