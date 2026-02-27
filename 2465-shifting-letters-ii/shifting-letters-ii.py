class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr=[0]*(len(s)+1)
        ans="" 
        for i in range(len(shifts)):
            if shifts[i][2]==0:
                arr[shifts[i][0]]-=1
                arr[shifts[i][1]+1]+=1
            elif shifts[i][2]==1: 
                arr[shifts[i][0]]+=1
                arr[shifts[i][1]+1]-=1
        prefix=[]
        prefix.append(arr[0])
        for i in range(1,len(arr)):
            prefix.append(arr[i]+prefix[i-1])
        for i in range(len(s)):
            ans+=chr((((ord(s[i])-ord('a')+prefix[i]))%26)+ord('a'))
        return ans
            # for j in range(shifts[i][0],shifts[i][1]+1):
            #     if shifts[i][2]==0:
            #         arr[j]=arr[j]-1
            #         if arr[j]<0:
            #             arr[j]=arr[j]+26
            #         elif arr[j]>25:
            #             arr[j]=arr[j]-26
            #     elif shifts[i][2]==1:
            #         arr[j]=arr[j]+1
            #         if arr[j]<0:
            #             arr[j]=arr[j]+26
            #         elif arr[j]>25:
            #             arr[j]=arr[j]-26
        # ans=[]
        # for i in arr:
        #     ans.append(chr(i+97))
        