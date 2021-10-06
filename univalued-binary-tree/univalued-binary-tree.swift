/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func isUnivalTree(_ root: TreeNode?) -> Bool {
        var val = root!.val
        return helper(root,val)
    }
    
    func helper(_ root: TreeNode?, _ val:Int) -> Bool {
        if let node = root {
            return node.val != val ? false : true && helper(node.left,val)
 && helper(node.right, val)        }
        return true
    }
}