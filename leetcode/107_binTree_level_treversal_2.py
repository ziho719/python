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
            res.insert(0,vals)                  #ez
            level=next