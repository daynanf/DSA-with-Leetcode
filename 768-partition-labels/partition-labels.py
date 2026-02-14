class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last=dict()
        for i in range(len(s)-1,-1,-1):
            if s[i] not in last:
                last[s[i]]=i

        ans=[]
        size=0
        end=0
        for i in range(len(s)):
            end=max(end,last[s[i]])
            size+=1
            if end==i:
                ans.append(size)
                size=0
        return ans
                

    

    
