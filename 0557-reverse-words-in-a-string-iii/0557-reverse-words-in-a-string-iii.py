class Solution:
    def reverseWords(self, s: str) -> str:
        st=""
        for wd in s.split():
            st+=(wd[::-1])+" "
        return st.strip()
        