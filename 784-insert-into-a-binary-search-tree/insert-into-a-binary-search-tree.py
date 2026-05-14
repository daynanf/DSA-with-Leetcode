# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(self,data):
            if self.val==None:
                self.val=data
            if self.val>data:
                if self.left:
                    insert(self.left,data)
                else:
                    self.left=TreeNode(data)
                    return
            elif self.val<data:
                if self.right:
                    insert(self.right,data)
                else:
                    self.right=TreeNode(data)
                    return
        if root:
            insert(root,val)
        else:
            root=TreeNode(val)
        return root  