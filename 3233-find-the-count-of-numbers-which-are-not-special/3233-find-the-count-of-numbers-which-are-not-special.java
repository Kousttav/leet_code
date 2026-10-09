
class Solution {
    public boolean check(int n) {
        if (n < 2) return false;

        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }

    public int nonSpecialCount(int l, int r) {
        int special = 0;

        int start = (int) Math.sqrt(l);
        int end = (int) Math.sqrt(r);

        for (int i = Math.max(2, start); i <= end; i++) {
            int square = i * i;

            if (square >= l && check(i)) {
                special++;
            }
        }

        return (r - l + 1) - special;
    }
}
