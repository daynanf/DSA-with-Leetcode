class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        # while x>0 and y>0:
        #     x-=1 #Alice
        #     y-=4
        #     if (x<=0) or (y<=3):
        #         return "Alice"
        #     x-=1 #Bob
        #     y-=4
        #     if x<=0 or y<=3:
        #         return "Bob"
        n=min(x,y//4)
        if n%2:
            return "Alice"
        else:
           return "Bob" 