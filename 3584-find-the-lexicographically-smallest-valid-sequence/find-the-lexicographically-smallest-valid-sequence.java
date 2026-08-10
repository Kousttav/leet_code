class Solution {
    public int[] validSequence(String word1, String word2) {
        int power = 1;
        int i=word1.length()-1;
        int j=word2.length()-1;
        List<Integer> l= new ArrayList<>();
        List<Integer> visited= new ArrayList<>();
        List<Integer> res= new ArrayList<>();
        int cnt=0;
        while (i>=0){
            if (j>=0 && word1.charAt(i)==word2.charAt(j)){
                cnt+=1;
                j-=1;
            }
            l.add(cnt);
            i-=1;
        }
        for(i=l.size()-1;i>=0;i--){
            visited.add(l.get(i));
        }
        j=0;
        for(i=0;i<word1.length();i++){
            if (j==word2.length())
                break;
            if (word1.charAt(i)!=word2.charAt(j) && power!=0){
                if (i!=word1.length()-1 && visited.get(i+1)>=word2.length()-j-1){
                    res.add(i);
                    power-=1;
                    j+=1;
                }
                else{
                    continue;
                }
            }
            else if(word1.charAt(i)!=word2.charAt(j) && power==0){
                continue;
            }
            else{
                res.add(i);
                j+=1;
            }
        }
        if (res.size() != word2.length()) {
            return new int[0];
        }

        int[] ans = new int[res.size()];
        for (i = 0; i < res.size(); i++) {
            ans[i] = res.get(i);
        }
        return ans;
    }
}