1class Solution:
2    def smallestSubsequence(self, s: str) -> str:
3        freq = {ch: 0 for ch in s}
4        vis = set()
5        stack = []
6
7        for ch in s:
8            freq[ch] += 1
9
10        for ch in s:
11            freq[ch] -= 1
12            if ch in vis:
13                continue
14            while stack and stack[-1] > ch and freq[stack[-1]] > 0:
15                vis.remove(stack.pop())
16            stack.append(ch)
17            vis.add(ch)
18
19        return "".join(stack)