1class Solution:
2    def reverseBits(self, n: int) -> int:
3        binary = bin(n)[2:].zfill(32)
4        binary = binary[::-1]
5        return int(binary, 2)