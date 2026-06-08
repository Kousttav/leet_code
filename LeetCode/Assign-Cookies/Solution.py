1class Solution:
2    def findContentChildren(self, g: List[int], s: List[int]) -> int:
3        g.sort()
4        s.sort()
5        child=cookie=0
6        while child<len(g) and cookie<len(s):
7            if s[cookie]>=g[child]:
8                child+=1
9            cookie+=1
10        return child