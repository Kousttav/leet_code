1class Solution:
2    def nthUglyNumber(self, n: int) -> int:
3        ugly = [1] 
4        i2, i3, i5 = 0, 0, 0  
5
6        while len(ugly) < n:
7            next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
8            ugly.append(next_ugly)
9            if next_ugly == ugly[i2] * 2:
10                i2 += 1
11            if next_ugly == ugly[i3] * 3:
12                i3 += 1
13            if next_ugly == ugly[i5] * 5:
14                i5 += 1
15
16        return ugly[n - 1]