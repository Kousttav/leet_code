1class Solution:
2    def smallestSubsequence(self, s: str) -> str:
3        vis = [0] * 26
4        num = [0] * 26
5
6        for ch in s:
7            num[ord(ch) - ord("a")] += 1
8        stk = []
9
10        for ch in s:
11            idx = ord(ch) - ord("a")
12            if not vis[idx]:
13                while stk and stk[-1] > ch:
14                    top_idx = ord(stk[-1]) - ord("a")
15                    if num[top_idx] > 0:
16                        vis[top_idx] = 0
17                        stk.pop()
18                    else:
19                        break
20                vis[idx] = 1
21                stk.append(ch)
22            num[idx] -= 1
23
24        return "".join(stk)