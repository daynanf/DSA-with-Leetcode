class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        num=target
        ans=0
        while num !=1:
            if num%2==0 and maxDoubles > 0:
                num/=2
                maxDoubles-=1
                ans+=1
            elif maxDoubles <= 0:
                ans+=num-1
                num=1
            else :
                num-=1
                ans+=1
        return int(ans)
