class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        count = len(intervals)
        prev_l = intervals[0][0]
        prev_r = intervals[0][1]
        for i in range(1, len(intervals)):
            # 1, 4,  2, 3
            if intervals[i][1] <= prev_r or intervals[i][0] == prev_l:
                count -= 1
            prev_l = intervals[i][0]
            prev_r = max(prev_r, intervals[i][1])
        return count