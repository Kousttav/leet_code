1class Solution {
2    public int[] fairCandySwap(int[] a, int[] b) {
3        Set<Integer> set=new HashSet();
4        int[] ans=new int[2];
5
6        int suma=0,sumb=0;
7        for(int i=0;i<a.length;i++)
8        suma+=a[i];
9        for(int j=0;j<b.length;j++){
10            sumb+=b[j];
11            set.add(b[j]);
12        }
13
14        int finalAns=(suma+sumb)/2;
15        for(int i=0;i<a.length;i++){
16            int value=finalAns-suma+a[i];
17            if(set.contains(value)){
18                ans[0]=a[i];
19                ans[1]=value;
20                return ans;
21            }
22        }
23    return ans;    
24    }
25}