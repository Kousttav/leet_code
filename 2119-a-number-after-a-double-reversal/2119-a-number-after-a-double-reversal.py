class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        x=int(str(num)[::-1])
        x=int(str(x)[::-1])
        return x==num
        