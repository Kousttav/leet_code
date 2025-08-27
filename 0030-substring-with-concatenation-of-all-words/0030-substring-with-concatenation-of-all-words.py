class Solution:
    def findSubstring(self, s: str, w: List[str]) -> List[int]:
        if not s or not w:
            return []

        wl, wl_total = len(w[0]), len(w) * len(w[0])
        wc = Counter(w)
        res = []

        for i in range(len(s) - wl_total + 1):
            seen = []
            for j in range(0, wl_total, wl):
                word = s[i + j:i + j + wl]
                seen.append(word)

            if Counter(seen) == wc:
                res.append(i)

        return res