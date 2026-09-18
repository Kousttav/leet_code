1class Solution:
2    def countEven(self, num: int) -> int:
3        total = 0
4        n = num
5
6        while n > 0:
7            total += n % 10
8            n //= 10
9
10        if total % 2 == 0:
11            return num // 2
12        else:
13            return (num - 1) // 2