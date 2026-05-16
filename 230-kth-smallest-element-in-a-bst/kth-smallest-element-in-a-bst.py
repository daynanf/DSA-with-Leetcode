# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def indorder(root):
            if root: 
                if root.left:
                    indorder(root.left)
                ans.append(root.val)
                if root.right:
                    indorder(root.right)
        indorder(root)
        ans.sort()
        return ans[k-1]