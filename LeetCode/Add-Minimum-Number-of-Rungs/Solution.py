1class Solution:
2    def addRungs(self, rungs: list[int], dist: int) -> int:
3        l=0
4        if rungs[0]>dist:
5            if dist>1:
6                l+=(rungs[0]-1)//dist
7            else:
8                l+=(rungs[0]-1)
9        for i in range(1,len(rungs)):
10            if (rungs[i]-rungs[i-1])>dist:
11                if dist>1:
12                    l+=(rungs[i]-rungs[i-1]-1)//dist
13                else:
14                    l+=(rungs[i]-rungs[i-1])-1
15                    print(l)
16        return l
17
18
19
20        