import java.util.Arrays;

class Solution {
    public boolean check(int[] nums) {
        int n = nums.length;

        int[] org = Arrays.copyOf(nums, n);
        Arrays.sort(org);

        StringBuilder st = new StringBuilder();
        StringBuilder s = new StringBuilder();
        for (int i = 0; i < 2 * n; i++) {
            st.append(nums[i % n]).append(",");
        }
        for (int num : org) {
            s.append(num).append(",");
        }

        return st.toString().contains(s.toString());
    }
}