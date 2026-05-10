class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        numBulls=0
        nonBullsG=[]
        nonBullsS=[]
        for i,x in enumerate(secret):
            if x==guess[i]:
                numBulls+=1
            else:
                nonBullsG.append(guess[i])
                nonBullsS.append(x)
        numCows=0
        countG={}
        countS={}
        for i in range(len(nonBullsG)):
            countG[nonBullsG[i]]=countG.get(nonBullsG[i],0)+1
        for i in range(len(nonBullsS)):
            countS[nonBullsS[i]]=countS.get(nonBullsS[i],0)+1
        for s in countG.keys():
            if countS.get(s,0)>=countG.get(s,0):
                numCows+=countG.get(s,0)
            elif countS.get(s,0)<countG.get(s,0):
                numCows+=countS.get(s,0)
        ans=f"{numBulls}A{numCows}B"
        return ans