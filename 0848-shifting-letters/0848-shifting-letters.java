
class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        int n = s.length();
        int[] l = new int[n];

        int sum = 0;

        for (int k = n - 1; k >= 0; k--) {
            sum = (sum + shifts[k] % 26) % 26;
            l[k] = sum;
        }

        StringBuilder ans = new StringBuilder(s);
        for (int i = 0; i < n; i++) {
            char ch = (char) (
                (s.charAt(i) - 'a' + l[i]) % 26 + 'a'
            );

            ans.setCharAt(i, ch);
        }

        return ans.toString();
    }
}
