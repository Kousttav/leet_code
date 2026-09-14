1class Solution:
2    def isPrefixString(self, s: str, words: List[str]) -> bool:
3        st=""
4        for wd in words:
5            st+=wd
6            if st == s:
7                return True
8        return False
9                
10        