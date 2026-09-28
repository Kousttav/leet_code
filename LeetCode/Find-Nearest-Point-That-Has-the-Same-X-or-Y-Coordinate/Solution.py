1class Solution:
2    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
3        result = -1
4        best = float("inf")
5
6        for i, (px, py) in enumerate(points):
7            if px == x or py == y:
8                distance = abs(x - px) + abs(y - py)
9                if distance < best:
10                    best = distance
11                    result = i
12
13        return result