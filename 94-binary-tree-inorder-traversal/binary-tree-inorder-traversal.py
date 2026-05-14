# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def indorder(root):
            if root: 
                if root.left:
                    indorder(root.left)
                ans.append(root.val)
                if root.right:
                    indorder(root.right)
        indorder(root)
        return ans