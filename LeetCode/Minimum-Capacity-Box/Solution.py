1class Solution:
2    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
3        # if max(capacity)<itemSize:
4        #     return -1
5        mx=-1
6        for i,n in enumerate(capacity):
7            if n<itemSize:
8                continue
9            if n==itemSize:
10                return i
11        
12            if mx == -1 or capacity[mx]>n:
13                mx=i
14        return mx
15        