class Solution:
    def reverse(self, x: int) -> int:
        temp=x
        if x<0:
            x*=-1
        s=0
        while x>0:
            r=x%10
            s=s*10+r
            x//=10
        if temp<0:
            s*=-1
        if s < -2**31 or s > 2**31 - 1: return 0
        return s

        