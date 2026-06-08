1class Solution {
2    public String convertToBase7(int num) {
3        if (num ==0)
4            return "0";
5        String l="";
6        boolean t=true;
7        if (num<0){
8            t=false;
9            num=num*-1;
10        }
11        while (num>0){
12            l+=num%7;
13            num/=7;
14        }
15        if (t==false)
16            l+="-";
17        String ans = "";
18        for (int i = l.length() - 1; i >= 0; i--) {
19            ans += l.charAt(i);
20        }
21
22        return ans;
23    }
24}