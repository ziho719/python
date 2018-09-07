class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # if preorder==[]:
        #     return None
        # root=TreeNode(preorder[0])
        # site=inorder.index(preorder[0])

        # root.left=self.buildTree(preorder[1:1+site],inorder[0:site])
        # root.right=self.buildTree(preorder[1+site:],inorder[site+1:])
        # return root

        if inorder==[]:
            return None
        root=TreeNode(preorder[0])
        site=inorder.index(preorder.pop(0))

        root.left=self.buildTree(preorder,inorder[0:site])
        root.right=self.buildTree(preorder,inorder[site+1:])
        return root