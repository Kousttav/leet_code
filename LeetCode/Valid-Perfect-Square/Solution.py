1class Solution:
2    def isPerfectSquare(self, x: int) -> bool:
3        r = x
4        while r * r > x:
5            r = (r + x // r) // 2
6        return r*r==x
7
8        