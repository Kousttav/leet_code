
import java.util.*;

class Solution {
    public long perfectPairs(int[] nums) {
        int n = nums.length;
        long[] arr = new long[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Math.abs((long) nums[i]);
        }

        Arrays.sort(arr);

        long count = 0;
        int right = 0;

        for (int left = 0; left < n; left++) {
            right = Math.max(right, left + 1);

            while (right < n && arr[right] <= 2L * arr[left]) {
                right++;
            }

            count += right - left - 1;
        }

        return count;
    }
}
