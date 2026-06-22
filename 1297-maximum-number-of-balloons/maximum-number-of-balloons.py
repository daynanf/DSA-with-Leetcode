class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        targetMap={}
        target="balloon"
        freq={}
        for i in range(len(target)):
            freq[target[i]]=freq.get(target[i],0)+1
        for i in range(len(target)):
            targetMap[target[i]]=targetMap.get(target[i],0)
        for i in range(len(text)):
            if text[i] in target:
                targetMap[text[i]]+=1
        ans=100000
        for i in targetMap:
            ans=min(ans,targetMap[i]//freq[i])
        return ans