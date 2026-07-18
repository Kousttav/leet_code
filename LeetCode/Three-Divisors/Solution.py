1class Solution:
2    def isThree(self, n: int) -> bool:
3        c=0
4        for i in range(1,n+1):
5            if n%i==0:
6                c+=1
7        return c==3