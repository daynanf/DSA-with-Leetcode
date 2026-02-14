class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for x in image:
            r=len(x)-1
            l=0
            while l<=r:
                x[l],x[r]=x[r],x[l] 
                l+=1
                r-=1
            for i in range(len(x)):
                x[i]=1-x[i]
        return image



