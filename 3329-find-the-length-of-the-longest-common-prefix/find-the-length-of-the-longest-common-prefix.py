class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        cont = 0
        prefix1 = set()
        prefix2 = set()
        for i in arr1:
            while i:
                prefix1.add(i)
                i=i//10
        for i in arr2:
            while i:
                prefix2.add(i)
                i=i//10
        for x in prefix1:
            if x in prefix2:
                s=str(x)
                l=len(s)
                cont=max(l,cont)
        return cont
