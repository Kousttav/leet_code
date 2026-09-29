1class Solution:
2    def addRungs(self, rungs: list[int], dist: int) -> int:
3        ans = 0
4        prev = 0
5
6        for rung in rungs:
7            gap = rung - prev
8
9            if gap > dist:
10                ans += (gap - 1) // dist
11
12            prev = rung
13
14        return ans