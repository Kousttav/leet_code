class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ch = {"2": list("abc"), "3": list("def"), "4": list("ghi"), "5": list("jkl"), "6":list("mno"), "7": list("pqrs"), "8": list("tuv"), "9": list("wxyz")}
        li = lt = ls = []
        st = ""
        if digits == "1" or digits == "":
            return []
        else:
            l = list(digits)
            li = lt = ch[l[0]]
            if len(l) == 1:
                return lt
            else:
                for i in range(1, len(l)):
                    ls = ch[l[i]]
                    lt = li
                    li = []
                    for j in lt:
                        st = ""
                        for k in ls:
                            st = j + k
                            li.append(st)
                return li