class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        if root.left is None and root.right is None:
            self.end=root
            return
        
        self.end=root
        # if root.left is not None:
        self.flatten(root.left)
        temp=self.end
        self.flatten(root.right)
        temp.right=root.right
        if root.left:
            root.right=root.left
        root.left=None

        return root


