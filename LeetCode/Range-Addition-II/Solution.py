1class Solution:
2    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
3        l1=m
4        l2=n
5
6        for a,b in ops:
7            l1=min(l1,a)
8            l2=min(l2,b)
9        return l1*l2