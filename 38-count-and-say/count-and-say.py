class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(n-1):
            count = 1
            tmp = ""
            for j in range(len(s)):
                if j == len(s) - 1 or s[j] != s[j+1]:
                    tmp += str(count) + s[j]
                    count = 1
                else:
                    count += 1
            s = tmp
        return s