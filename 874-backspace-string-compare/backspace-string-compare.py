class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sA=[]
        sB=[]
        for x in s:
            if not sA :
                if x != "#":
                    sA.append(x)
            elif x != "#":
                    sA.append(x)
            else:
                sA.pop()
        for x in t:
            if not sB:
                if x != "#":
                    sB.append(x)
            elif x != "#":
                    sB.append(x)
            else:
                sB.pop()
        return sA==sB