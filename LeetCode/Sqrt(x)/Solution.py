1class Solution:
2    def mySqrt(self, x: int) -> int:
3        r = x
4        while r * r > x:
5            r = (r + x // r) // 2
6        return r
7