class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_pattern = [s.index(c) for c in s]
        t_pattern = [t.index(c) for c in t] 
        return s_pattern == t_pattern