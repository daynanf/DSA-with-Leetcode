class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt=0
        for i in range(len(hours)):
            for j in range(i+1,len(hours)):
                if not (hours[i]+hours[j])%24:
                    cnt+=1
        return cnt