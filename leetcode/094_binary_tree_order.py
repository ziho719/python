class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        if root:
            if root.left:
                res+=self.inorderTraversal(root.left)
            res.append(root.val)
            if root.right:
                res.extend(self.inorderTraversal(root.right))
        return res
    
s=Solution()
t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)
t4=TreeNode(4)
t1.left=None
t1.right=t2
t2.left=t3
t2.right=t4

print(s.inorderTraversal(t1))