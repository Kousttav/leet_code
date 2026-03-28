class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        l=[]
        for i in licensePlate:
            if i.isalpha():
                l.append(i.lower())
        # print(l)
        c=Counter(l)
        # print(c)
        words.sort(key=len)
        for w in words:
            if all(c[i] <= w.count(i) for i in c):
                return w