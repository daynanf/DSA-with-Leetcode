class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        i=2*(n-1)
        a=k%i 
        if a<n:
            return a
        else:
             return 2*n-a-2