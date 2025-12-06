class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l = sorted(set(arr)) 
        rank = {}
        i = 1
        for n in l: 
            rank[n] = i
            i += 1
        result = []
        for num in arr:
            r = rank[num]
            result.append(r)   
        return result