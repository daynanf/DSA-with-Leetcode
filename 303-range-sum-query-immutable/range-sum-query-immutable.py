class NumArray:

    def __init__(self, nums: List[int]):
        n=len(nums)+1
        self.p=[0]*n
        self.p[1]=nums[0]
        for i in range (1,n-1):
            self.p[i+1]=nums[i]+self.p[i]


    def sumRange(self, left: int, right: int) -> int:
        return self.p[right+1]-self.p[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)