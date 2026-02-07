class Solution:
    def kthCharacter(self, k: int) -> str:
        word="a"
        while len(word) < k:
            temp=""
            for i in word:
                temp+= chr(ord(i) + 1)
            word+=temp
        return word[k-1]