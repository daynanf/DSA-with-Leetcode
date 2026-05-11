class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for x in nums:
            digits=[]
            while x:
                d=x%10
                digits.append(d)
                x=x//10
            digits.reverse()
            ans.extend(digits)
        return ans