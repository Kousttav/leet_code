class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        b=s.split()
        for i in b:
            if i.isalpha()==False:
                b.pop(i)
        return len(b[len(b)-1])
        