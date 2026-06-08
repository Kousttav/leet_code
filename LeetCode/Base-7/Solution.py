1class Solution:
2    def convertToBase7(self, num: int) -> str:
3        if num ==0:
4            return "0"
5        l=[]
6        t=True
7        if num<0:
8            t=False
9            num=num*-1
10        while num>0:
11            l.append(str(num%7))
12            num//=7
13        if t==False:
14            l.append("-")
15        return "".join(l[::-1])
16        