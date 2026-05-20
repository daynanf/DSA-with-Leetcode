class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        while left<=right:
            dLeft=str(left)
            isSelfD=False
            for x in dLeft:
                if int(x)==0 or left%int(x)!=0:
                    isSelfD=False
                    break
                elif left%int(x)==0:
                    isSelfD=True
            if isSelfD:
                ans.append(left)
            left+=1

        return ans