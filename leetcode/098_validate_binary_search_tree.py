class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if self.help(root):
            return True
        return False

    def help(self,root):
        """
        rtype: (int max,int min)  or False
        """
        if root==None:
            #空子树为真,可以避免这一条
            return True  
        elif root.left==None and root.right==None:
            return (root.val,root.val)
        
        max=min=root.val

        if root.left:
            leftpair=self.help(root.left)
            if leftpair:
                if leftpair[1]>=root.val:
                    return False
            else:
                return False
            min=leftpair[0]
        if root.right:
            rightpair=self.help(root.right)
            if rightpair:
                if rightpair[0]<=root.val:
                    return False
            else:
                return False
            max=rightpair[1]

        return (min,max)

s=Solution()
t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)
t2.left=t1
t2.right=t3   

print(s.isValidBST(t2))

