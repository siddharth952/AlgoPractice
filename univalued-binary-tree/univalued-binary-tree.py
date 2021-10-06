# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        dq = collections.deque([root])
        while dq:
            node = dq.popleft()
            if (node.val) != root.val:
                return False
            dq.extend([n for n in (node.left,node.right) if n])
            
        return True