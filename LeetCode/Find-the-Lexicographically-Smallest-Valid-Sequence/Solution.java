1class Solution {
2    public int[] validSequence(String word1, String word2) {
3        int power = 1;
4        int i=word1.length()-1;
5        int j=word2.length()-1;
6        List<Integer> l= new ArrayList<>();
7        List<Integer> visited= new ArrayList<>();
8        List<Integer> res= new ArrayList<>();
9        int cnt=0;
10        while (i>=0){
11            if (j>=0 && word1.charAt(i)==word2.charAt(j)){
12                cnt+=1;
13                j-=1;
14            }
15            l.add(cnt);
16            i-=1;
17        }
18        for(i=l.size()-1;i>=0;i--){
19            visited.add(l.get(i));
20        }
21        j=0;
22        for(i=0;i<word1.length();i++){
23            if (j==word2.length())
24                break;
25            if (word1.charAt(i)!=word2.charAt(j) && power!=0){
26                if (i!=word1.length()-1 && visited.get(i+1)>=word2.length()-j-1){
27                    res.add(i);
28                    power-=1;
29                    j+=1;
30                }
31                else{
32                    continue;
33                }
34            }
35            else if(word1.charAt(i)!=word2.charAt(j) && power==0){
36                continue;
37            }
38            else{
39                res.add(i);
40                j+=1;
41            }
42        }
43        if (res.size() != word2.length()) {
44            return new int[0];
45        }
46
47        int[] ans = new int[res.size()];
48        for (i = 0; i < res.size(); i++) {
49            ans[i] = res.get(i);
50        }
51        return ans;
52    }
53}