# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans=False
        def isSame(root1,root2):
            right=left=True
            if root1 and root2:
                if root1.val!=root2.val:
                    return False
                if root1.left and root2.left:
                    left = isSame(root1.left,root2.left)
                if root1.right and root2.right:
                    right = isSame(root1.right,root2.right)
                if (root1.left and not root2.left) or (root2.left and not root1.left):
                    return False
                if (root1.right and not root2.right) or (root2.right and not root1.right):
                    return False 
                if (root1.left is None and root1.right is None) and (root2.left is None and root2.right is None):
                    if root1.val!=root2.val:
                        return False
                    else:
                        return True
                return left and right
            elif (root1 and not root2) or (root2 and not root1):
                return False
            else:
                return True
        ans=isSame(p,q)
        return ans