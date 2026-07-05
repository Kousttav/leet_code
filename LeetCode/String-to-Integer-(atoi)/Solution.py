1class Solution:
2    def myAtoi(self, s: str) -> int:
3        s=s.strip()
4        result = 0
5        i=0
6        sign=1
7        if(s and s[i] in '+-'):
8            if s[i]=='-':
9                sign=-1
10            else:
11                sign=1
12            i+=1
13
14        while i < len(s) and s[i].isdigit():
15            result = result * 10 + int(s[i]) 
16            i += 1
17        result *= sign 
18        if result < -2**31: return -2**31 
19        elif result > 2**31 - 1: return 2**31 - 1 
20        return result
21s='   -042'
22sol=Solution()
23print(sol.myAtoi(s))