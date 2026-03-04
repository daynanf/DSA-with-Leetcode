class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        sumd=0
        while n:
            d=n%10
            prod*=d
            sumd+=d
            n=n//10
        return prod-sumd