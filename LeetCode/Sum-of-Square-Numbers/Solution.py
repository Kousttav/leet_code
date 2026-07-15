1import math
2
3class Solution:
4    def judgeSquareSum(self, c: int) -> bool:
5        left = 0
6        right = math.isqrt(c)
7
8        while left <= right:
9            s = left * left + right * right
10
11            if s == c:
12                return True
13            elif s < c:
14                left += 1
15            else:
16                right -= 1
17
18        return False