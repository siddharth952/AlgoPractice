# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        while root:
            if root.left != None:
                pre = root.left
                while(pre.right and pre.right != root):
                    pre = pre.right
                
                if not pre.right:
                    pre.right = root
                    res.append(root.val)
                    root = root.left
                
                else:
                    pre.right = None
                    root = root.right
            
            else:
                res.append(root.val)
                root = root.right
        
        return res