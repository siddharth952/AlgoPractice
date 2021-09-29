class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        _The_Fox_jumped_ _=space
        
        We need the len of last word in s
        '''
        N = len(s)
        ans, i = 0, N-1
        
        while s[i] == ' ':
            i -= 1
        while s[i] != ' ' and i>=0:
            ans += 1
            i -= 1
        
        return ans