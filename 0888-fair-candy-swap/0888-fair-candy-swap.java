class Solution {
    public int[] fairCandySwap(int[] a, int[] b) {
        Set<Integer> set=new HashSet();
        int[] ans=new int[2];

        int suma=0,sumb=0;
        for(int i=0;i<a.length;i++)
        suma+=a[i];
        for(int j=0;j<b.length;j++){
            sumb+=b[j];
            set.add(b[j]);
        }

        int finalAns=(suma+sumb)/2;
        for(int i=0;i<a.length;i++){
            int value=finalAns-suma+a[i];
            if(set.contains(value)){
                ans[0]=a[i];
                ans[1]=value;
                return ans;
            }
        }
    return ans;    
    }
}