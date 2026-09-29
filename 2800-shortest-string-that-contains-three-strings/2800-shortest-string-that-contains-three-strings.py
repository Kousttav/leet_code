class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(s,t):
            idx=-1
            for i in range(len(s)):
                left,right=i,0
                while(left<len(s) and right<len(t)):
                    if s[left]==t[right]:
                        left+=1
                        right+=1
                    else:
                        break
                    
                if left == len(s):
                    idx=right
                    break
                if right == len(t):
                    return s
            if idx==-1:
                return s+t

            return s+t[idx:]

        def f(a, b, c):
            finalstr = merge(a, b)
            finalstr = merge(finalstr, c)
            return finalstr


        strings = [
            f(a, b, c),
            f(a, c, b),
            f(b, a, c),
            f(b, c, a),
            f(c, b, a),
            f(c, a, b)
        ]

        size = float('inf')
        answer = ""

        for s in strings:
            if len(s) < size:
                answer = s
                size = len(s)
            elif len(s) == size:
                answer = min(answer, s)

        return answer
