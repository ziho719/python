class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        #过了，存了一个hashmap导致比较慢

        #改进：ex存int------->直接存node

        #Todo: 再改进的话是-->help不必回传(node,node)的元组，记录一个pre为根元素

        #以及，这个help写的时候没有条理，想到什么就写什么了

        #所以这个思路非常多余<---记录左右子树的最大最小

        self.ex1=TreeNode(100000000000)
        self.ex2=TreeNode(-10000000000)
        self.help(root)
        self.ex1.val,self.ex2.val=self.ex2.val,self.ex1.val

    def help(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        low=up=root
        if root:
            if root.left:
                lf=self.help(root.left)
                if root.val<=lf[1].val:
                    if lf[1].val>self.ex2.val:
                        self.ex2=lf[1]
                    if root.val<self.ex1.val:
                        self.ex1=root
                if lf[0].val<low.val:
                    low=lf[0]
                if lf[1].val>up.val:
                    up=lf[1]
            if root.right:
                rf=self.help(root.right)
                if root.val>=rf[0].val:
                    if rf[0].val<self.ex1.val:
                        self.ex1=rf[0]
                    if root.val>self.ex2.val:
                        self.ex2=root

                if rf[0].val<low.val:
                    low=rf[0]
                if rf[1].val>up.val:
                    up=rf[1]
                
                
            if not root.left and not root.right:
                return (root,root)
        return (low,up)

class Solution2:
    """
    别人的简洁的代码
    !!!!因为中序遍历的性质prev一直是前一个数！！！！！！！NB,TM想多了
    """
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = None  #

    def recoverTree(self, root):
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        if self.prev and self.prev.val > node.val:
            if self.first is None:
                self.first = self.prev
            self.second = node
        self.prev = node
        self.inorder(node.right)


s=Solution2()
t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)

t1.left=t3
t3.right=t2

s.recoverTree(t1)