1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        for ch in ransomNote:
4            if ch not in magazine:
5                return False
6            magazine = magazine.replace(ch, "", 1)
7        return True