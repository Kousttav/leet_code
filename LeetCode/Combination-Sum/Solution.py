1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res = []
4        def backtrack(rem, combo, start):
5            if rem < 0:
6                return
7            elif rem == 0:
8                res.append(list(combo))
9                return
10            for i in range(start, len(candidates)):
11                combo.append(candidates[i])
12                backtrack(rem - candidates[i], combo, i)
13                combo.pop()
14
15        backtrack(target, [], 0)
16        return res