class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        '''
        For Each window of s2, of len(s1) we want to check if cnt of window is == cnt of s1
        cnt of string is (no. of a's, num of b's etc...)
        
        
        we maintain the window by del. the values of s2[i-len(s1)] when it gets larger than len(s1)
        
        After this we would need to check if it's equal to target
        
        list values instead of 'a' 'z' makes it easier.
        
        
        '''
        A = [ord(x) - ord('a') for x in s1] # ab
        B = [ord(x) - ord('a') for x in s2] # hhhhabhhh
        
        # Count
        target = [0] * 26
        for x in A: 
            target[x] += 1
            
        window = [0] * 26
        for i,x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[ B[i-len(A)] ] -= 1 # Reduce the window
            
            if window == target:
                return True
        
        return False
         
        