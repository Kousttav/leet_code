class Solution:
    def sortMatrix(self, grid):
        n = len(grid)
        for r in range(n):
            diag = []
            i=r
            j=0
            while i < n and j < n:
                diag.append(grid[i][j])
                i += 1
                j += 1
            diag.sort()
            i=r
            j=0
            while i < n and j < n:
                grid[i][j] = diag.pop()
                i += 1
                j += 1
        for c in range(1, n):
            diag = []
            i=0
            j=c
            while i < n and j < n:
                diag.append(grid[i][j])
                i += 1
                j += 1
            diag.sort(reverse=True)
            i=0
            j=c
            while i < n and j < n:
                grid[i][j] = diag.pop()
                i += 1
                j += 1
        return grid 