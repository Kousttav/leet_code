class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new=s.split(" ")
        if len(pattern) != len(new):
            return False
        p=[]
        for i in pattern:
            if i not in p:
                p.append(i)
                
        if len(p)!=len(set(new)):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = new[i]
        new_s=""
        for i in pattern:
            new_s=new_s+" "+d[i]
        return new_s.strip()==s


        