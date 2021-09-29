class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        1. Subproblems
        can climb 1 or 2 steps 
        
        Total ways to climb to top
        
        '''
        a=b = 1
        for _ in range(n):
            a,b = b, a+b
        
        return a
        