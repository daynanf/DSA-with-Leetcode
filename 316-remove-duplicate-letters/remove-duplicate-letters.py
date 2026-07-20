class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq= dict()
        for x in s:
           freq[x] = freq.get(x,0)+1
        ans=[]
        for x in s:
            if  not ans:
                ans.append(x)
                freq[x]-=1
                continue                
            elif x in set(ans):
                freq[x]-=1
                continue                               
            while ans and ans[-1] > x and freq[ans[-1]] > 0:
                ans.pop()
            ans.append(x)
            freq[x]-=1
        return "".join(ans)