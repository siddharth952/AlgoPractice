class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            "abcabcbb" used={a:3,b:1,c:2}
              s
                i
             
             mx=3
             
        
        '''
    
        start = maxLength = 0
        used = {}
        
        for i, c in enumerate(s):
            if c in used and start <= used[c]: # start <= usedChar[s[i]] to make sure we don't worry that 'pwwp' we won't miss w and go straight to p by this
                start = used[c] + 1
            else:
                maxLength = max(maxLength, i-start +1)
            
            used[c] = i
        
        return maxLength
                
                
        