class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words_s1 = s1.split()
        words_s2 = s2.split()
        c=[]
        for w in words_s1:
            if words_s1.count(w) == 1 and w not in words_s2:
                c.append(w)
        for w in words_s2:
            if words_s2.count(w) == 1 and w not in words_s1:
                c.append(w)
        return c
        