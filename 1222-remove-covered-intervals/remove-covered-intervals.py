class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        covered = [False] * len(intervals)

        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i != j:
                    if (intervals[j][0] <= intervals[i][0] and
                        intervals[i][1] <= intervals[j][1]):
                        covered[i] = True
                        break

        return covered.count(False)