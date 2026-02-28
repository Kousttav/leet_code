class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper = 0
        
        for ch in word:
            if ord('A') <= ord(ch) <= ord('Z'):
                upper += 1
        
        if upper == len(word):          # all uppercase
            return True
        if upper == 0:                  # all lowercase
            return True
        if upper == 1 and ord('A') <= ord(word[0]) <= ord('Z'):  # first uppercase
            return True
        
        return False