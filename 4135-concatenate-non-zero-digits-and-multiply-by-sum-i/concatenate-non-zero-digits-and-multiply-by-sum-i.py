class Solution:
    def sumAndMultiply(self, n: int) -> int:
        strN=str(n)
        nonZero=[]
        for i in range(len(strN)):
            if strN[i] != "0":
                nonZero.append(strN[i])
        if len(nonZero) == 0:
            return 0
        sumD=0
        for i in range(len(nonZero)):
            sumD+=int(nonZero[i])
        x=int("".join(nonZero))
        return x*sumD