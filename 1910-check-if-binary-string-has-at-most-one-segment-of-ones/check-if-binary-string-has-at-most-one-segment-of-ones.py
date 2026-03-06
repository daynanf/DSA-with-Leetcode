class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cnt=0
        if len(s)==1 or "0" not in s:
            return True
        for i in range(len(s)-1):
            if (s[i]=="0" and s[i+1]=="1") or (s[i]=="1" and s[i+1]=="0") :
                cnt+=1
        return True if cnt==1 else False