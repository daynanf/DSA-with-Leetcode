class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        res = ""
        for target in range(1, 27):  
            lower = [0] * 26
            upper = [0] * 26
            l = 0
            distinct = 0
            complete = 0
            for r in range(n):
                ch = s[r]
                idx = ord(ch.lower()) - ord('a')
                if ch.islower():
                    if lower[idx] == 0 and upper[idx] == 0:
                        distinct += 1
                    lower[idx] += 1
                    if lower[idx] == 1 and upper[idx] > 0:
                        complete += 1
                else:
                    if lower[idx] == 0 and upper[idx] == 0:
                        distinct += 1
                    upper[idx] += 1
                    if upper[idx] == 1 and lower[idx] > 0:
                        complete += 1
                while distinct > target:
                    ch = s[l]
                    idx = ord(ch.lower()) - ord('a')
                    if ch.islower():
                        if lower[idx] == 1 and upper[idx] > 0:
                            complete -= 1
                        lower[idx] -= 1
                        if lower[idx] == 0 and upper[idx] == 0:
                            distinct -= 1
                    else:
                        if upper[idx] == 1 and lower[idx] > 0:
                            complete -= 1
                        upper[idx] -= 1
                        if lower[idx] == 0 and upper[idx] == 0:
                            distinct -= 1
                    l += 1
                if distinct == complete:
                    if r - l + 1 > len(res):
                        res = s[l:r+1]
        return res