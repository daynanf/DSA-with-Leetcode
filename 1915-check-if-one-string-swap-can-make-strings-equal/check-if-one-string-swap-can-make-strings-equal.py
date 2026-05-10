class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        oddCnt=0
        odd1=[]
        odd2=[]
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                oddCnt+=1
                odd1.append(s1[i])
                odd2.append(s2[i])

        return True if (oddCnt==2 or oddCnt==0)  and set(odd2) == set(odd1) else False