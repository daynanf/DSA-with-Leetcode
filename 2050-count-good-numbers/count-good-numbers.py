class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m=1000000007
        
        def spow(x,n):
            ans=1
            while n>0:
                if n%2:
                    ans*=x%m
                x*=x%m
                n//=2
            return ans
       
        if n%2!=0:
            a=spow(5,abs(n//2))
            b=spow(4,abs(n//2))
            return ((a*b)*5)%m
        else:
            a=spow(5,abs(n//2))
            b=spow(4,abs(n//2))
            return (a*b)%m
        
        
        
        
        
        
        
        if n>0 and n%2!=0:
            return (self.countGoodNumbers(n-1)*5)%(1000000007)
        elif n>0 and n%2==0:
            return (self.countGoodNumbers(n-1)*4)%(1000000007)
        else: 
            return 1
        