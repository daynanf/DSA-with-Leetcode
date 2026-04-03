class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num5=num10=num20=0
        for i in range(len(bills)):
            if bills[i]==5:
                num5+=1
            elif bills[i]==10:
                num10+=1
                num5-=1
                if num5<0:
                    return False
            else:
                num20+=1
                if num10:
                    if num5:
                        num10-=1
                        num5-=1
                    else:
                        return False
                else:
                    if num5>=3:
                        num5-=3
                    else:
                        return False
                    
        return True