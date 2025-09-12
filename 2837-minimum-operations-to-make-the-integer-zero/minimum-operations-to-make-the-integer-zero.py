class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(60):
            target = num1-k*num2
            if target.bit_count() <= k and target >= k:
                return k
        return -1