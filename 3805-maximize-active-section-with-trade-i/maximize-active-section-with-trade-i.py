class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        if s.count("0") <= 1 or s.count("1") < 1 :
            return s.count("1")
        zeroArr=[]
        groupZero=0
        for i, x in enumerate(s):
            if x=="0":
                groupZero+=1
                if i+1<len(s) and s[i+1] =="1":
                    zeroArr.append(groupZero)
                    groupZero=0
        if groupZero > 0 and not zeroArr  :
            return s.count("1")    
        elif groupZero > 0 and zeroArr:
            zeroArr.append(groupZero)
        elif groupZero <= 0 and len(zeroArr)==1:
             return s.count("1")  

        ans=[]
        for i,x in enumerate(zeroArr):
            if i<len(zeroArr)-1:
                ans.append(x + zeroArr[i+1])
            else:
                ans.append(x)
        return max(ans) + s.count("1")