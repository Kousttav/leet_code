class Solution:
    def clearStars(self, s: str) -> str:
        ns=[[] for _ in range(26)]
        a=list(s)
        for i,c in enumerate(a):
            if c == "*":
                for k in range(26):
                    if ns[k]:
                        a[ns[k].pop()]="*"
                        break
            else:
                ns[ord(c) - ord("a")].append(i)

        l=[]
        for c in a:
            if c != "*":
                l.append(c)
        return "".join(l)
            
        