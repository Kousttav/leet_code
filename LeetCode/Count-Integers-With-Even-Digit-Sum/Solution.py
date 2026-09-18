1class Solution:
2    def countEven(self, num: int) -> int:
3        c=0
4        def check(n):
5            n=str(n)
6            s=0
7            for i in n:
8                s+=int(i)
9            return s
10        for i in range(1,num+1):
11            if check(i)%2==0:
12                c+=1
13        return c
14
15            
16
17        