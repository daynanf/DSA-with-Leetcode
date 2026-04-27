class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        empty=numBottles
        while empty>=numExchange:
            x=empty//numExchange
            ans+=x
            empty=empty%numExchange+x
        return ans