class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        while len(nums) > 1:
            n = len(nums)
            new_nums = []
            
            for i in range(n // 2):
                if i % 2 == 0:
                    new_nums.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    new_nums.append(max(nums[2 * i], nums[2 * i + 1]))
            nums = new_nums
            
        return nums[0]