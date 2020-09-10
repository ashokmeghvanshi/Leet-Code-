class Solution:
    def reverseBits(self, n: int) -> int:
        l=32-len(bin(n)[2:])
        s='0'*l+bin(n)[2:]
        return int(s[::-1],2)
