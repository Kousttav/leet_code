class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new=s.split(" ")
        w={}
        if len(pattern)!=len(new):
            return False
        for i in range(len(new)):
            if new[i] not in w:
                w[new[i]]=pattern[i]
            elif w[new[i]]!=pattern[i]:
                return False
        return len(set(w.keys()))==len(set(w.values()))