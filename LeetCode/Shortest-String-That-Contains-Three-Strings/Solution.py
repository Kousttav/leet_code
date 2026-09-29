1class Solution:
2    def minimumString(self, a: str, b: str, c: str) -> str:
3        def merge(s,t):
4            idx=-1
5            for i in range(len(s)):
6                left,right=i,0
7                while(left<len(s) and right<len(t)):
8                    if s[left]==t[right]:
9                        left+=1
10                        right+=1
11                    else:
12                        break
13                    
14                if left == len(s):
15                    idx=right
16                    break
17                if right == len(t):
18                    return s
19            if idx==-1:
20                return s+t
21
22            return s+t[idx:]
23
24        def f(a, b, c):
25            finalstr = merge(a, b)
26            finalstr = merge(finalstr, c)
27            return finalstr
28
29
30        strings = [
31            f(a, b, c),
32            f(a, c, b),
33            f(b, a, c),
34            f(b, c, a),
35            f(c, b, a),
36            f(c, a, b)
37        ]
38
39        size = float('inf')
40        answer = ""
41
42        for s in strings:
43            if len(s) < size:
44                answer = s
45                size = len(s)
46            elif len(s) == size:
47                answer = min(answer, s)
48
49        return answer
50