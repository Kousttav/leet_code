from collections import deque

class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:

        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        m = len(grid)
        n = len(grid[0])

        q = deque()
        q.append((0, 0))

        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        while q:
            r, c = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions[grid[r][c]]:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:

                    if not visited[nr][nc]:

                        # Check reverse direction
                        if (-dr, -dc) in directions[grid[nr][nc]]:

                            visited[nr][nc] = True
                            q.append((nr, nc))

        return False