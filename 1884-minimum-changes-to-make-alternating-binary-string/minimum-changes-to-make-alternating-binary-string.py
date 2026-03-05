class Solution:
    def minOperations(self, s: str) -> int:
        prev=s[0]
        cnt=0
        for i in range(1,len(s)):
            if s[i]==prev:
                cnt+=1
                prev= "1" if prev=="0" else "0"
            else:
                prev=s[i]
        return min(cnt,len(s)-cnt)

