1class Solution:
2    def addDigits(self, num: int) -> int:
3        if num == 0:
4            return 0
5
6        while num >= 10:
7            l = []
8
9            while num > 0:
10                l.append(num % 10)
11                num //= 10
12
13            num = sum(l)
14
15        return num