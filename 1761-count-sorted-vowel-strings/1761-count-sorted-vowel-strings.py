from itertools import combinations_with_replacement
class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels=['a','e','i','o','u']
        li=[''.join(p) for p in combinations_with_replacement(vowels,n)]
        return len(li)
n=33
sol=Solution()
print(sol.countVowelStrings(n))
        
        