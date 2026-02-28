class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        for i in range(0, len(s), 2*k):
            nw = s[i:i+k]
            rem = s[i+k:i+2*k]
            st = ""
            for ch in nw:
                st = ch + st 
            
            ans = ans + st + rem
        
        return ans