class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        f=True
        st = ""
        for i in range(0, len(s), k):
            if f:
                st+=s[i:i+k][::-1]
                f=False      
            else:
                st+=s[i:i+k]
                f=True
        return st