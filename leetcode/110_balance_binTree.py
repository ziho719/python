class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if self.helper(root):
                return True
        else:
            return True

        return False
        
    def helper(self,root):
        if root is None:
            return 0
        
        l=self.helper(root.left)
        r=self.helper(root.right)

        if l is False or r is False:
            return False

        if not (-2<l-r<2):
            return False
        else:
            return max(l,r)+1
        