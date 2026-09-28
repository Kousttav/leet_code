1class Solution:
2    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
3        d=[]
4        for a,b in points:
5            if a==x or b==y:
6                d.append(abs(a - x) + abs(b - y))
7            else:
8                d.append(float('inf'))
9        
10        i=min(d)
11        if i == float('inf'):
12            return -1
13        print(i)
14        for j in range(len(d)):
15            if d[j]==i:
16                return j
17                
18        