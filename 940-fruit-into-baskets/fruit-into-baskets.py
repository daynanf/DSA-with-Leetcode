class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        count = {}
        max_len = 0
        for r in range(len(fruits)):
            count[fruits[r]] = count.get(fruits[r], 0) + 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len