class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c=Counter(words[0])
        for w in words[1:]:
            c&=Counter(w)
        result=[]
        for key,value in c.items():
            result.extend([key]*value)
        return result

        