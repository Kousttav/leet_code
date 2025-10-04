class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l=[]
        def permutations(elements, curr=[]):
            if not elements and curr not in l:
                l.append(curr)
            else:
                for i in range(len(elements)):
                    new = elements[i]
                    rem_elements = elements[:i] + elements[i+1:]
                    permutations(rem_elements, curr + [new])
        permutations(nums)
        return l