1class Solution:
2    def isPowerOfThree(self, n: int) -> bool:
3        if n <= 0:
4            return False
5        while n % 3 == 0:
6            n //= 3
7        return n == 1
8        