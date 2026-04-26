class Solution:
    def myPow(self, x: float, n: int) -> float:
        def spow(x,n):
            ans=1
            while n>0:
                if n%2:
                    ans*=x
                x*=x
                n//=2
            return ans
        ans=spow(x,abs(n))
        return ans if n>0 else 1/ans

        
             