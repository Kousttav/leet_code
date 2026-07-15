1import math
2class Solution:
3    def judgeSquareSum(self, c: int) -> bool:
4        for a in range(math.isqrt(c) + 1):
5            rem = c - a * a
6            if math.isqrt(rem) ** 2 == rem:
7                return True
8        return False