class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res=[]
        level=[root]

        while True:
            if level==[]:
                return res
            vals=[]
            next=[]
            for node in level:
                vals.append(node.val)
                if node.left is not None:
                    next.append(node.left)
                if node.right is not None:
                    next.append(node.right)                
            res.append(vals)
            level=next

s=Solution()
t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)
t4=TreeNode(4)
t5=TreeNode(5)
t2.left=t1
t2.right=t3   
t3.left=t4
t3.right=t5


print(s.levelOrder(t2))

        