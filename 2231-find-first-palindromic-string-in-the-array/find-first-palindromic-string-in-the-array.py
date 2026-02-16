class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for x in words:
            cnt=0
            r=len(x)-1
            for l in range(len(x)//2):
                if x[l]==x[r]:
                    cnt+=1
                r-=1
            if cnt==len(x)//2:
                return x
        return ""