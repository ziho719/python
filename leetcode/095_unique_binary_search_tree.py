import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution2:
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
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """    
        if n==0:
            return []
        if n==1:
            return [TreeNode(1)]
        
        self.hash={}       
        return self.helper(n,1)
        
    def helper(self,n,numStart):
        """
        type n: int    剩余节点数目
        type numStart: int 
        type dad；TreeNode
        rtype:List[TreeNode] 
        """
        #生成左节点，再生成根结点，再生成右结点

        #没有记忆的程序用时700ms

        #加入hashtable 提供记忆后400ms

        #不需要deepcopy,去掉后60ms
        res=[]
        if n==0:
            return [None]
        if n==1:
            return [TreeNode(numStart)]
        if (n,numStart) in self.hash:
            return self.hash[(n,numStart)]
               
        for i in range(numStart,numStart+n):
            
            leftTreeList=self.helper(i-numStart,numStart)
            rightTreeList=self.helper(numStart+n-1-i,i+1)

            for ln in leftTreeList:
                for rn in rightTreeList:
                    thisRoot=TreeNode(i)
                    thisRoot.left=ln
                    thisRoot.right=rn
                    res.append(thisRoot)
        self.hash[(n,numStart)]=res
        return res
            
            
        
s=Solution()
s2=Solution2()
t=s.generateTrees(3)
for i in t:
    print(s2.inorderTraversal(i))

       