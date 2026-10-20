class Solution {
    public String removeStars(String s) {
        Stack<Character> st = new Stack<>();
        for(char c : s.toCharArray()){
            if(c!='*')
                st.push(c);
            else
                st.pop();
        }
        String res="";
        while(st.isEmpty()==false){
            res=st.pop()+res;
        }
        return res;
    }
}