class Solution {
    public int pivotIndex(int[] nums) {
        int l = 0;
        int r = 0;
        for(int num : nums) 
            r += num;
        for (int i = 0; i < nums.length; i++) {
            r-=nums[i];
            if (l==r){return i;}
            l+=nums[i];
        }
        return -1;
    }
}
