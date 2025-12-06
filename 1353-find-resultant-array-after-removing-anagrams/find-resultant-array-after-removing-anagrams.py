from collections import Counter
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if not words:
            return []
        r= [words[0]]
        l= tuple(sorted(words[0]))

        for i in range(1, len(words)):
            c= tuple(sorted(words[i]))
            if c != l:
                r.append(words[i])
                l= c
        return r