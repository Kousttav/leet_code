1class Solution:
2    def numJewelsInStones(self, jewels: str, stones: str) -> int:
3        l=[i for i in jewels]
4        print(l)
5        c=0
6        for i in stones:
7            if i in l:
8                c+=1
9        return c