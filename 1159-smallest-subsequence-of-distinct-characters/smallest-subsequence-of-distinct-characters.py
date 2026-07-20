class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq= dict()
        for x in s:
            freq[x] = freq.get(x,0)+1
        ans=[]
        visited=set()
        for x in s:
            freq[x]-=1
            if  not ans:
                ans.append(x)
                visited.add(x)
                continue                
            elif x in visited:
                continue                               
            while ans and ans[-1] > x and freq[ans[-1]] > 0:
                r=ans.pop()
                visited.remove(r)
            ans.append(x)
            visited.add(x)
        return "".join(ans)  