class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverseN(n):
            num=[]
            ans=0
            if n<10:
                return n
            else:
                while n:
                    d=n%10  
                    num.append(d)
                    n=n//10
                for i in range(len(num)-1,-1,-1):
                    ans+=num[i]*(10**(len(num)-i-1))
                return ans

        return abs(n-reverseN(n))