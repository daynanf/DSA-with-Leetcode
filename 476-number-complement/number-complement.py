class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1 
        num_bits = num.bit_length()
        mask = (1 << num_bits) - 1
        return num ^ mask  