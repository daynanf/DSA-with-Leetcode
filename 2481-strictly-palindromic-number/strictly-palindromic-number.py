class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        x=n-2
        if (x+2==n):
            return False