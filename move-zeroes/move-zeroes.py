class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.https://leetcode.com/problems/move-zeroes/discuss/
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                # Swap
                nums[slow], nums[fast] = nums[fast], nums[slow]
            
            # wait for a non zero to swap with zero
            if nums[slow] != 0:
                slow += 1