class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l=0
        res=0
        window=0
        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
            freqM = max(count.values())
            window+=1
            if window - freqM <= k:
                res=max(res,window)
            else:
                count[s[l]]=count.get(s[l],0)-1
                l+=1
                window-=1
        return res




