1class Solution:
2    def countAndSay(self, n: int) -> str:
3        s = "1"
4        for i in range(n-1):
5            count = 1
6            tmp = ""
7            for j in range(len(s)):
8                if j == len(s) - 1 or s[j] != s[j+1]:
9                    tmp += str(count) + s[j]
10                    count = 1
11                else:
12                    count += 1
13            s = tmp
14        return s