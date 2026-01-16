class Solution:
    def isValid(self, word: str) -> bool:
        v=0
        c=0
        word=word.lower()
        for i in word:
            if not i.isalnum():     
                    return False     
            if i.isalpha():
                if i in ('a', 'e', 'i', 'o', 'u'):
                    v+=1
                else:
                    c+=1
        return v>=1 and c>=1 and len(word)>=3