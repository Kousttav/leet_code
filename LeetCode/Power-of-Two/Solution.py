1class Solution:
2    def isPowerOfTwo(self, n: int) -> bool:
3        if n<=0:
4            return False
5        return (n & (n-1))==0
6        