1class Solution:
2    def findFinalValue(self, nums: List[int], n: int) -> int:
3        while True:
4            if n in nums:
5                n=n*2
6            else:
7                return n
8        