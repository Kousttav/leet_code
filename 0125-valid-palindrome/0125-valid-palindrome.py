class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        st=""
        for ch in s:
            if ch.isalnum():
                st+=ch
        if st==st[::-1]:
            return True
        else:
            return False
        