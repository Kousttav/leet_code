1class Solution:
2    def isPowerOfTwo(self, n: int) -> bool:
3        if n <= 0:
4            return False
5        while n % 2 == 0:
6            n //= 2
7        return n == 1
8        