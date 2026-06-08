class Solution {
    public String licenseKeyFormatting(String s, int k) {
        StringBuilder sb = new StringBuilder();
        int len = s.length();
        int j =0; // count
        for(int i =len-1; i>=0; i--){
            char ch = s.charAt(i);
            if(ch!='-'){
                if(j ==k){
                    j =0;
                    sb.append('-');
                }
                if(Character.isAlphabetic(ch))
                    ch = Character.toUpperCase(ch);
                sb.append(ch);
                j++;
            }
        }
        return sb.reverse().toString();
    }
}