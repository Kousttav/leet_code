class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # banned.append(" ")
        nw=""
        for wd in paragraph:
            if wd.isalpha() or wd==" ":
                nw+=wd
            else:
                nw+=" "
        nw=nw.lower().split()
        d={}
        for i in nw:
            if i not in d:
                d[i]=1
            else:
                d[i]+=d[i]
        print(d)
        for i in set(banned):
            if i in d.keys():
                d.pop(i)
        return max(d,key=d.get)