class Solution:
    def reverseWords(self, s: str) -> str:
        my_list=s.split(" ")
        st=[item.strip() for item in my_list]
        st=st[::-1]
        stz=""
        for ch in st:
            if ch!='':
                stz=stz+" "+ch
        return stz.strip()