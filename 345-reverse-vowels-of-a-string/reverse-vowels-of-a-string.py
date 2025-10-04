class Solution:
    def reverseVowels(self, s: str) -> str:
        L=list(s)
        i,j=0,len(L)-1
        while i<j:
            if L[i] in 'AEIOUaeiou':
                while L[j] not in "AEIOUaeiou":
                    j-=1
                if L[j] in "AEIOUaeiou" and i<j:
                    L[i],L[j]=L[j],L[i]
                    j-=1
            i+=1        
        return ''.join(L)