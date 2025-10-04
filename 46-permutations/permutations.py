class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l=[]
        def get_permutations_recursive(elements, current_permutation=[]):
            if not elements:
                l.append(current_permutation)
            else:
                for i in range(len(elements)):
                    new_element = elements[i]
                    remaining_elements = elements[:i] + elements[i+1:]
                    get_permutations_recursive(remaining_elements, current_permutation + [new_element])
        get_permutations_recursive(nums)
        return l