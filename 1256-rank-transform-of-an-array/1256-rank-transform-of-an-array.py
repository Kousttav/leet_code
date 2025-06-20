class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l = sorted(set(arr)) 
        rank = {}
        i = 1
        for n in l: 
            rank[n] = i
            i += 1
        return [rank[n] for n in arr]
