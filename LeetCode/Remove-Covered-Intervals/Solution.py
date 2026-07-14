1class Solution:
2    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
3        covered = [False] * len(intervals)
4
5        for i in range(len(intervals)):
6            for j in range(len(intervals)):
7                if i != j:
8                    if (intervals[j][0] <= intervals[i][0] and
9                        intervals[i][1] <= intervals[j][1]):
10                        covered[i] = True
11                        break
12
13        return covered.count(False)