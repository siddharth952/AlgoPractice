"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, t1: 'Node') -> 'Node':
        if not t1:
            return t1
        
        
        def populate(lvls):
            for i in range(len(lvls)-1): lvls[i].next = lvls[i+1]
        
        
        q = deque([t1])
                
        while(q):
            if not any(q):
                return t1
            
            
            curr = []
            for node in q:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            
            populate(q)
            q = curr
            
            
        return t1