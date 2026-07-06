1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        res = []
4        while matrix:
5            res.extend(matrix.pop(0))
6            matrix = [*zip(*matrix)][::-1]
7        return res