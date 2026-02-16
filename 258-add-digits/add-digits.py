class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            n=num
            s=0
            while n:
                s+=n%10
                n//=10
            num=s
        return num