class Solution:
    def isPerfectSquare(self, x: int) -> bool:
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r*r==x

        