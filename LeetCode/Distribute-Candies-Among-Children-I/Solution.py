1class Solution:
2    def distributeCandies(self, n: int, limit: int) -> int:
3        count = 0
4
5        for i in range(min(n, limit) + 1):
6            for j in range(min(n - i, limit) + 1):
7
8                k = n - i - j
9                if 0 <= k <= limit:
10                    count += 1
11
12        return count