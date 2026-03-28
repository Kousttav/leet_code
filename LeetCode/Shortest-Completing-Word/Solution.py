1class Solution:
2    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
3        l=[]
4        for i in licensePlate:
5            if i.isalpha():
6                l.append(i.lower())
7        # print(l)
8        c=Counter(l)
9        # print(c)
10        words.sort(key=len)
11        for w in words:
12            if all(c[i] <= w.count(i) for i in c):
13                return w