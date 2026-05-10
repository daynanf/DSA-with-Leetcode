class Solution:
    def countPoints(self, rings: str) -> int:
        colors=defaultdict(list)
        for i in range(1,len(rings),2):
            colors[rings[i]].append(rings[i-1])
        ans=0
        RGB=set(['R','G','B'])
        for i in colors.keys():
            if set(colors[i])==RGB:
                ans+=1
        return ans