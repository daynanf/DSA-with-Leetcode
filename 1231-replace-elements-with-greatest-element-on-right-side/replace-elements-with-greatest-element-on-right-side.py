class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[]
        posM=-1
        Mnum=0
        for i in range(len(arr)-1):
            if i>=posM:
                Mnum=0
                for j in range(i+1,len(arr)): 
                    if arr[j]>Mnum:
                        posM=j
                        Mnum=arr[j]
                ans.append(Mnum)
            else:
                ans.append(Mnum)
        ans.append(-1)
        return ans