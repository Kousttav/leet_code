class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        st=""
        for wd in words:
            st+=wd
            if st == s:
                return True
        return False
                
        