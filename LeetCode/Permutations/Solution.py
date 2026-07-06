1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        l=[]
4        def permutations(elements, curr=[]):
5            if not elements:
6                l.append(curr)
7            else:
8                for i in range(len(elements)):
9                    new = elements[i]
10                    rem_elements = elements[:i] + elements[i+1:]
11                    permutations(rem_elements, curr + [new])
12        permutations(nums)
13        return l