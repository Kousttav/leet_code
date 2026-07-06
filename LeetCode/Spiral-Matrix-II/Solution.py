1class Solution:
2    def generateMatrix(self, n: int) -> list[list[int]]:
3        matrix = [[0] * n for _ in range(n)]
4        
5        left, right, top, bottom = 0, n - 1, 0, n - 1
6        num = 1
7        
8        while left <= right and top <= bottom:
9           
10            for col in range(left, right + 1):
11                matrix[top][col] = num
12                num += 1
13            top += 1
14            
15            
16            for row in range(top, bottom + 1):
17                matrix[row][right] = num
18                num += 1
19            right -= 1
20            
21        
22            if top <= bottom:
23                for col in range(right, left - 1, -1):
24                    matrix[bottom][col] = num
25                    num += 1
26                bottom -= 1
27            
28            
29            if left <= right:
30                for row in range(bottom, top - 1, -1):
31                    matrix[row][left] = num
32                    num += 1
33                left += 1
34        
35        return matrix