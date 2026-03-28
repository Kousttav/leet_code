1class Solution:
2    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
3        words_s1 = s1.split()
4        words_s2 = s2.split()
5        c=[]
6        for w in words_s1:
7            if words_s1.count(w) == 1 and w not in words_s2:
8                c.append(w)
9        for w in words_s2:
10            if words_s2.count(w) == 1 and w not in words_s1:
11                c.append(w)
12        return c
13        