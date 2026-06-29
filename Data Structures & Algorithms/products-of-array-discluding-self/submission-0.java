class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        if (len == 0)
            return new int[] {};
        int[] lt = new int[len];
        int[] rt = new int[len];
        int[] sol = new int[len];
        lt[0] = 1;
        rt[len - 1] = 1;

        for (int i = 1; i < len; i++) {
            lt[i] = nums[i - 1] * lt[i - 1];
        }
        for (int i = len-2; i >= 0; i--) {
            rt[i] = nums[i +1 ] * rt[i + 1];
        }
        for (int i = 0; i < len; i++) {
            sol[i] = lt[i] * rt[i];
        }
        return sol;
    }
}
