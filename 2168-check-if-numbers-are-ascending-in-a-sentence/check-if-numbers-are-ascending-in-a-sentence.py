class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        res=True
        last=0
        for ch in s.split():
            if ch.isdigit():
                if last<int(ch):
                    last=int(ch)
                else:
                    res=False
                    break
        return res
