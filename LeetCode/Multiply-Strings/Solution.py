1class Solution:
2    def multiply(self, num1: str, num2: str) -> str:
3        result1=result2 = 0
4        for char in num1:
5            if '0' <= char <= '9':
6                digit1 = ord(char) - ord('0')
7                result1 = result1 * 10 + digit1
8        print(result1)
9        result = 0
10        for ch in num2:
11            if '0' <= ch <= '9':
12                digit2 = ord(ch) - ord('0')
13                result2 = result2 * 10 + digit2
14        print(result2)
15        return str(result1*result2)
16
17        