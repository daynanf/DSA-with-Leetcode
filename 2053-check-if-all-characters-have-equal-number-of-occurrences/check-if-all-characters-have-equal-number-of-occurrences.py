class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq={}
        for x in s:
            freq[x]=freq.get(x,0)+1
        return len(set(freq.values()))==1