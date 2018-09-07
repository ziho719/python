class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        #ez while 105 is done well

        if inorder==[]:
            return None
        root=TreeNode(postorder[-1])
        site=inorder.index(postorder.pop())

        root.right=self.buildTree(inorder[site+1:],postorder)
        root.left=self.buildTree(inorder[0:site],postorder)
        return root