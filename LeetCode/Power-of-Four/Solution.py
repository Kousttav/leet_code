1class Solution:
2    def isPowerOfFour(self, n: int) -> bool:
3        if n<=0:
4            return False
5        while n%4==0:
6            n=n//4
7        return n==1        