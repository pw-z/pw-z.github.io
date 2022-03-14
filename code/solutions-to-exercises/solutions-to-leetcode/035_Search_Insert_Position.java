class Solution {
    /**
     * 二分查找，此题区别在于查找不到的情况下需要给出应该插入的位置
     * 需要一个变量记录上一次的方向
     * 
     * @param nums
     * @param target
     * @return
     */
    public static int searchInsert(int[] nums, int target) {
        int low = 0;
        int high = nums.length-1;
        int ans = nums.length; //中间值一直小于target，最终target需要放在最后一个位置即nums.length
        while (low <= high) {
            int mid = (high-low)/2 +low;
            if(nums[mid] >= target){
                ans = mid;
                high = mid -1;
            }else{
                low = mid +1;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int [] nums = {1, 4, 5};
        System.out.println(searchInsert(nums, 2));
    }
}