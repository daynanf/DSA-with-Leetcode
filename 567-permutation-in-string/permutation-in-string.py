class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1=[0]*26
        freq2=[0]*26
        l=0
        if len(s1)>len(s2):
            return False
        for x in s1:
            freq1[ord(x)-ord('a')]+=1
        for i in range(len(s2)):
            if i+1<=len(s1):
                freq2[ord(s2[i])-ord('a')]+=1
            else:
                freq2[ord(s2[i])-ord('a')]+=1
                freq2[ord(s2[l])-ord('a')]-=1
                l+=1
            if freq1==freq2:
                return True
        return False
            