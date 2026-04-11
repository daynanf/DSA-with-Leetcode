class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr=[]
        ans=0
        n=len(costs)
        for c in costs:
            diff=c[1]-c[0]
            arr.append([diff,c[0],c[1]])
        arr.sort(reverse=True)
        for i in range(len(arr)):
            if i< n/2:
                ans+=arr[i][1]
            else:
                ans+=arr[i][2]
        return ans


        