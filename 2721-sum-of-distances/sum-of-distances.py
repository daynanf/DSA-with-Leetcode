class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        arrS=defaultdict(list)
        ansDict=defaultdict(list)
        preDict=defaultdict(list)
        ans=[]
        for i,x in enumerate(nums):
            arrS[x].append(i+1)
        for x in arrS.keys():
            preDict[x].append(0)
            for n in arrS[x]:
                preDict[x].append((preDict[x][-1]+n))
            for i,n in enumerate(arrS[x]):
                preSum=preDict[x][i]
                postSum=preDict[x][-1]-preDict[x][i+1]
                a=((i*n)-preSum)+(postSum-n*(len(arrS[x])-i-1))
                ansDict[x].append(a)
            ansDict[x].reverse()
        for  n in nums:
            x=ansDict[n].pop()
            ans.append(x)
        return ans  

        