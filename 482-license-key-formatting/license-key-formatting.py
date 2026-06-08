class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        st = s.replace("-", "").upper()

        res = ""
        cnt = 0

        for i in range(len(st) - 1, -1, -1):
            res += st[i]
            cnt += 1

            if cnt == k and i != 0:
                res += "-"
                cnt = 0

        return res[::-1]