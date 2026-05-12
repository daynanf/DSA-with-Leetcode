class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans=0
        digits=[]
        while n:
            d=n%10
            digits.append(d)
            n=n//10
        digits.reverse()
        for i in range(len(digits)):
            if i%2:
                ans-=digits[i] 
            else:
                ans+=digits[i]
        return ans