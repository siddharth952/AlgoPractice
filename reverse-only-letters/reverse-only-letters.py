class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        N = len(s)
        ans = [None] * N
        stack = []
        
        for i,c in enumerate(s):
            if c.isalpha():
                stack.append(c)
            else:
                ans[i] = c
        
        for i,c in enumerate(s):
            if c.isalpha():
                ans[i] = stack.pop()
        
        return ''.join(ans)