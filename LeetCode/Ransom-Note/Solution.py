1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        
4        for i in set(ransomNote):
5            if magazine.count(i) - ransomNote.count(i) < 0:
6                return False
7        return True