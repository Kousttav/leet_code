class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        a = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                a.append(grid[i][j])

        a.reverse()
        k = k%len(a)
        a[:k] = a[:k][::-1]
        a[k:] = a[k:][::-1]
        b = [a[i*len(grid[0]):(i+1)*len(grid[0])] for i in range(len(grid))]
        return b