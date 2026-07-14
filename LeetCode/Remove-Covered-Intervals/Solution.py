1class Solution:
2    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key = lambda x:x[0])
4        count = len(intervals)
5        prev_l = intervals[0][0]
6        prev_r = intervals[0][1]
7        for i in range(1, len(intervals)):
8            # 1, 4,  2, 3
9            if intervals[i][1] <= prev_r or intervals[i][0] == prev_l:
10                count -= 1
11            prev_l = intervals[i][0]
12            prev_r = max(prev_r, intervals[i][1])
13        return count