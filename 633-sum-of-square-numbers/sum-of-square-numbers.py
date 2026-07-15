import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(math.isqrt(c) + 1):
            rem = c - a * a
            if math.isqrt(rem) ** 2 == rem:
                return True
        return False