from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque()
        q.append((entrance[0], entrance[1]))

        maze[entrance[0]][entrance[1]] = '+'   # Mark entrance as visited
        steps = 0

        while q:
            size = len(q)

            for _ in range(size):
                x, y = q.popleft()

                if (x, y) != (entrance[0], entrance[1]) and (
                    x == 0 or x == m - 1 or y == 0 or y == n - 1
                ):
                    return steps

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and maze[nx][ny] != '+'
                    ):
                        q.append((nx, ny))
                        maze[nx][ny] = '+'   # Mark as visited

            steps += 1

        return -1