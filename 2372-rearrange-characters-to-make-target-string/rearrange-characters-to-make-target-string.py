class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        targetMap={}
        freq={}
        for i in range(len(target)):
            freq[target[i]]=freq.get(target[i],0)+1
        for i in range(len(target)):
            targetMap[target[i]]=targetMap.get(target[i],0)
        for i in range(len(s)):
            if s[i] in target:
                targetMap[s[i]]+=1
        ans=101
        for i in targetMap:
            ans=min(ans,targetMap[i]//freq[i])
        return ans