class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        element=list(range(1,n+1))
        com=combinations(element,k)
        # result=[list(c) for c in com]
        return list(com)