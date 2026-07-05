1class Solution:
2    def isSameAfterReversals(self, num: int) -> bool:
3        x=int(str(num)[::-1])
4        x=int(str(x)[::-1])
5        return x==num
6        