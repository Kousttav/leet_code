class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m = len(mat)
        n = len(mat[0])

        diagonal = []

        direction = 1

        i, j = 0, 0

        for _ in range(m * n):
            diagonal.append(mat[i][j])

            if direction == 1:
                if j == n - 1:
                    i += 1
                    direction = -1
                elif i == 0:
                    j += 1
                    direction = -1
                else:
                    i -= 1
                    j += 1
            else:
                if i == m - 1:
                    j += 1
                    direction = 1
                elif j == 0:
                    i += 1
                    direction = 1
                else:
                    i += 1
                    j -= 1

        return diagonal