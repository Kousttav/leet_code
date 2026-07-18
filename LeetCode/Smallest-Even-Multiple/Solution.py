1class Solution:
2    def smallestEvenMultiple(self, n: int) -> int:
3        if n%2!=0:
4            return n*2
5        return n
6        