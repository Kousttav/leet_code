class Solution {
    public String convertToBase7(int num) {
        if (num ==0)
            return "0";
        String l="";
        boolean t=true;
        if (num<0){
            t=false;
            num=num*-1;
        }
        while (num>0){
            l+=num%7;
            num/=7;
        }
        if (t==false)
            l+="-";
        String ans = "";
        for (int i = l.length() - 1; i >= 0; i--) {
            ans += l.charAt(i);
        }

        return ans;
    }
}