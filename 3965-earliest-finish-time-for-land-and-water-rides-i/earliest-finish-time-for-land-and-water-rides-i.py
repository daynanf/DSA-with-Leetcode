class Solution:
        def earliestFinishTime(self, startL: List[int], durL: List[int], startW: List[int], durW: List[int]) -> int:
            minL, minW, res = 3000, 3000, 3000
            n = len(startL)
            m = len(startW)

            for i in range(n):
                minL = min(minL, startL[i] + durL[i])

            for i in range(m):
                minW = min(minW, startW[i] + durW[i])
                res = min(res, max(minL, startW[i]) + durW[i])

            for i in range(n):
                res = min(res, max(minW, startL[i]) + durL[i])

            return res