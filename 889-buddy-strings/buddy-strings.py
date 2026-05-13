class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        oddCnt=0
        odd1=[]
        odd2=[]
        for i in range(min(len(s),len(goal))):
            if s[i] != goal[i]:
                oddCnt+=1
                odd1.append(s[i])
                odd2.append(goal[i])
        if  len(set(s))<len(s) and s == goal:
             return True
        return True if oddCnt==2 and set(odd2) == set(odd1) and len(s)==len(goal) else False