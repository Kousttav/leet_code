class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        for row in grid:
            row.insert(0, 0)
            row. append(0)

        grid.insert(0, [0]*len(grid[0]))
        grid.append([0]*len(grid[0]))

        perimeter = 0

        for i in range(1, row_len + 1):
            for j in range(1, col_len +1):
                if grid[i][j] == 1:
                    if grid[i-1][j] == 0:
                        perimeter += 1
                    if grid[i+1][j] == 0:
                        perimeter += 1
                    if grid[i][j-1] == 0:
                        perimeter += 1
                    if grid[i][j+1] == 0:
                        perimeter += 1

        return perimeter