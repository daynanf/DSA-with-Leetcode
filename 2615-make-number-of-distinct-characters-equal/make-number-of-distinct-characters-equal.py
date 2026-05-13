class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        freq1={}
        freq2={}
        for x in word1:
            freq1[x]=freq1.get(x,0)+1
        for x in word2:
            freq2[x]=freq2.get(x,0)+1        
        distinct1=len(freq1)
        distinct2=len(freq2)
        for a in freq1:
            for b in freq2:

                new1 = distinct1
                new2 = distinct2
                if a == b:
                    if new1 == new2:
                        return True
                    continue

                if freq1[a] == 1:
                    new1 -= 1

                if b not in freq1:
                    new1 += 1
                if freq2[b] == 1:
                    new2 -= 1
                if a not in freq2:
                    new2 += 1

                if new1 == new2:
                    return True

        return False