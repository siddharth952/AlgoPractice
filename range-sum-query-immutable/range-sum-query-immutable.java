class NumArray {
    int[] preSum;
    public NumArray(int[] nums) {
        preSum = nums; // Pass by pointer
        preSum[0] = nums[0];
        for(int i=1; i<preSum.length; i++)
            preSum[i] += preSum[i-1];
    }
    
    public int sumRange(int left, int right) {
        if ( left == 0)
            return preSum[right];
        else{
            return preSum[right] - preSum[left-1];
        }
    }
}