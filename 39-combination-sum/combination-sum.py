class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp =[]
        def backtrack(rem, combo, start):
            if rem < 0:
                return
            elif rem == 0:
                res.append(list(combo))
                return
            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                backtrack(rem - candidates[i], combo, i)
                combo.pop()

        backtrack(target,temp, 0)
        return res