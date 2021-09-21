# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not t1 or not t2: return t1 or t2
        q = deque( [(t1,t2)] )
        while q:
            n1 , n2 = q.popleft()
            
            # Nothing to add from t2's node
            if not n2:
                continue
            
            n1.val += n2.val
            
            # No node check
            if not n1.left and n2.left: n1.left = TreeNode(0)
            if not n1.right and n2.right: n1.right = TreeNode(0)
                
            q.append( (n1.right, n2.right) )
            q.append( (n1.left, n2.left) )
        
        return t1
        
        
                
                
                