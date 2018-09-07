import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.nums=[]
        self.res=[]
        self.helper(root,sum)
        return self.res
    def helper(self, root, sum):
        if root is None:
            return False
        
        self.nums.append(root.val)

        if root.left is None and root.right is None:
            if sum==root.val:
                self.res.append(copy.deepcopy(self.nums))

        self.helper(root.left,sum-root.val)
        self.helper(root.right,sum-root.val)

        self.nums.pop()