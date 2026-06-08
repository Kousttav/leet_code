1class Solution {
2    public int findContentChildren(int[] g, int[] s) {
3        Arrays.sort(g);
4        Arrays.sort(s);
5        int child=0, cookie=0;
6        while (child<g.length && cookie<s.length){
7            if (s[cookie]>=g[child])
8                child+=1;
9            cookie+=1;
10        }
11        return child;
12    }
13}