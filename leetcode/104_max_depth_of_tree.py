class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.deep=0
        self.max=0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.deep+=1
            self.max=max(self.deep,self.max)
        else:
            return 
        self.maxDepth(root.left)
        self.maxDepth(root.right)
        self.deep-=1

        if self.deep==0:
            return self.max


        