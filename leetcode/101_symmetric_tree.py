class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.helper(root.left,root.right) and self.helper(root.right,root.left)

    
    def helper(self,ta,tb):
        if ta is None and tb is None:
            return True
        elif ta is None or tb is None:
            return False
        
        if ta.val!=tb.val:
            return False
        
        return self.helper(ta.left,tb.right) and self.helper(ta.right,tb.left)
            