1class Solution:
2    def arrayRankTransform(self, arr: List[int]) -> List[int]:
3        l = sorted(set(arr)) 
4        rank = {}
5        i = 1
6        for n in l: 
7            rank[n] = i
8            i += 1
9        result = []
10        for num in arr:
11            r = rank[num]
12            result.append(r)   
13        return result