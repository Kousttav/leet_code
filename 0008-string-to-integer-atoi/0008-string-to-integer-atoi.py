class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        result = 0
        i=0
        sign=1
        if(s and s[i] in '+-'):
            if s[i]=='-':
                sign=-1
            else:
                sign=1
            i+=1

        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i]) 
            i += 1
        result *= sign 
        if result < -2**31: return -2**31 
        elif result > 2**31 - 1: return 2**31 - 1 
        return result
s='   -042'
sol=Solution()
print(sol.myAtoi(s))