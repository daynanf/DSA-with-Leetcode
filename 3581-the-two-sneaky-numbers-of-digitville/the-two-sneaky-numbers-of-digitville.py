class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen=set()
        duplicate=set()
        for x in nums:
            if x in seen:
                duplicate.add(x)
            else:
                seen.add(x)
        return list(duplicate)