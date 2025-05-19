class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        b=s[::-1]
        for i in range(len(b)):
            s[i]=b[i]

        