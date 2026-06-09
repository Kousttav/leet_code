1class Solution:
2    def isPowerOfThree(self, n: int) -> bool:
3        if n<=0:
4            return False
5            
6        while n%3==0:
7            n=n//3
8
9        if n==1:
10            return True
11        else:
12            return False
13        