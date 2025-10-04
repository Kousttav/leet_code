class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result1=result2 = 0
        for char in num1:
            if '0' <= char <= '9':
                digit1 = ord(char) - ord('0')
                result1 = result1 * 10 + digit1
        print(result1)
        result = 0
        for ch in num2:
            if '0' <= ch <= '9':
                digit2 = ord(ch) - ord('0')
                result2 = result2 * 10 + digit2
        print(result2)
        return str(result1*result2)

        