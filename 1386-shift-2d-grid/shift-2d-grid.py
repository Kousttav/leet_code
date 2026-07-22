class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r=len(grid)
        c=len(grid[0])
        for i in range(k):
            a=grid[r-1][c-1]
            b=grid[0][0]
            for j in range(1,r*c):
                bd=grid[j//c][j%c]
                grid[j//c][j%c]=b
                b=bd
            grid[0][0]=a
        return grid
        