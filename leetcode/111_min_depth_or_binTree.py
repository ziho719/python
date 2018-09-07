class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.deep=0
        self.min=100
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.deep+=1
            if root.left is None and root.right is None:
                self.min=min(self.deep,self.min)
        else:           
            if self.deep==0:
                return 0
            return
        self.minDepth(root.left)
        self.minDepth(root.right)
        self.deep-=1

        if self.deep==0:
            return self.min