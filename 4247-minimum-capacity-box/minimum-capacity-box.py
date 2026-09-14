class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        if max(capacity)<itemSize:
            return -1
        mx=-1
        for i,n in enumerate(capacity):
            if n<itemSize:
                continue
            if n==itemSize:
                return i
        
            if mx == -1 or capacity[mx]>n:
                mx=i
        return mx
        