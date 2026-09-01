class Solution:
    def checkString(self, s: str) -> bool:
        p=len(s)
        for i,wd in enumerate(s):
            if wd=="b":
                p=i
                break
        print(p)
        st=s[p:]
        return "a" not in st

        