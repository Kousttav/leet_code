1class Solution:
2    def findShortestSubArray(self, nums: List[int]) -> int:
3        d=defaultdict(list)
4        for i,j in enumerate(nums):
5            d[j].append(i)
6        # print(d)
7        m=0
8        for v in d.values():
9            m=max(m,len(v))
10        print(m)
11
12        b = len(nums)
13        for v in d.values():
14            # print(len(v))
15            if len(v) == m:
16                b = min(b,v[-1]-v[0]+1)
17            # print(b)
18        return b