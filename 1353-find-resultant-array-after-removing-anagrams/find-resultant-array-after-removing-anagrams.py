class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        l=[]
        l.append(words[0])
        for i in range (1,len(words)):
            if sorted(words[i])!=sorted(l[-1]):
                l.append(words[i])
        return l