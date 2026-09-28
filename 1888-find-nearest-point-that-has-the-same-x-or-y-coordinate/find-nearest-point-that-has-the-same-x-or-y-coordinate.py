class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        result = -1
        best = float("inf")

        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                distance = abs(x - px) + abs(y - py)
                if distance < best:
                    best = distance
                    result = i

        return result