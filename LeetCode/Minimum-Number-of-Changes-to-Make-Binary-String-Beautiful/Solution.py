1class Solution:
2    def minChanges(self, s: str) -> int:
3        answer = 0
4        for i in range(0, len(s), 2):
5            if s[i] != s[i + 1]:
6                answer += 1
7        return answer
8        