class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cnt=0
        prevEnd = intervals[0][1]
        for l,r in intervals[1:]:
            if l>=prevEnd:
                prevEnd=r
            else:
                cnt+=1
                prevEnd=min(r,prevEnd)
            
        return cnt
        
        return 