class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        max_gap = 0
        last_pos = None
        for i, bit in enumerate(binary):
            if bit == '1':
                if last_pos is not None:
                     max_gap = max(max_gap, i - last_pos)
                last_pos = i
            
        return max_gap