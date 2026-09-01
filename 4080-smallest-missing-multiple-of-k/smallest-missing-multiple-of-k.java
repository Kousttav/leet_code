class Solution {
    public int missingMultiple(int[] nums, int k) {

        int idx = 1;

        while (true) {
            int target = k * idx;
            boolean found = false;

            for (int num : nums) {
                if (num == target) {
                    found = true;
                    break;
                }
            }

            if (!found) {
                return target;
            }

            idx++;
        }
    }
}