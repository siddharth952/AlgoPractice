class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Two numbers add to target
        Sorted in ASC
        
        [2,7,11,15] target = 9
        
        '''
        
        l,r = 0,len(nums)-1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l+1,r+1]
            elif s > target: # We know its sorted hence  go left
                r -= 1
            else:
                l += 1
        
        return -1
        
        '''
        [2,7,11,15] tar = 9
        l        r         s = 17 s>target, r--
        
        [2,7,11,15]
        l     r         s = 13 s > target r--
        
        [2,7,11,15]    s = 9 s==target return
        l  r
        
        
        [2,3,4]  target = 7    s = 6 s<target l++
           l  r
        
        [2,3,4] s = 7 equal
           l r
        '''