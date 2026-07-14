1class Solution:
2    def arrayRankTransform(self, arr: List[int]) -> List[int]:
3        sorted_unique = sorted(set(arr)) 
4        rank_map = {}
5        index = 1
6        for num in sorted_unique: 
7            rank_map[num] = index
8            index += 1
9        return [rank_map[num] for num in arr]
10