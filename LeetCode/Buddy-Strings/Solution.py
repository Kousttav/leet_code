1class Solution:
2    def buddyStrings(self, s: str, goal: str) -> bool:
3        if len(s) != len(goal):
4            return False
5
6        if s == goal:
7            seen_chars = set ()
8            for char in s:
9                if char in seen_chars:
10                    return True
11                seen_chars.add(char)
12            return False
13        d = []
14        for i in range(len(s)):
15            if s[i] != goal[i]:
16                d.append(i)
17
18        if len(d) == 2:
19            i, j = d
20            if s[i] == goal[j] and s[j] == goal[i]:
21                return True
22
23        return False
24        