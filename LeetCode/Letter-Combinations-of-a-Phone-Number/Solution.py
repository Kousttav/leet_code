1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        ch = {"2": list("abc"), "3": list("def"), "4": list("ghi"), "5": list("jkl"), "6":list("mno"), "7": list("pqrs"), "8": list("tuv"), "9": list("wxyz")}
4        li = lt = ls = []
5        st = ""
6        if digits == "1" or digits == "":
7            return []
8        else:
9            l = list(digits)
10            li = lt = ch[l[0]]
11            if len(l) == 1:
12                return lt
13            else:
14                for i in range(1, len(l)):
15                    ls = ch[l[i]]
16                    lt = li
17                    li = []
18                    for j in lt:
19                        st = ""
20                        for k in ls:
21                            st = j + k
22                            li.append(st)
23                return li