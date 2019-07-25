class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        if root.left:
            self.helper(root.left,root)
        elif root.right:
            self.helper(root.right,root)
            
    def helper(self,node,prevLevel):
        thisNode = node
        prev=prevLevel
        if node is not None:
            while prev:
                if prev.left:
                    if prev.left!=thisNode:  
                        thisNode.next=prev.left
                        thisNode=prev.left
                if prev.right:
                    if prev.right!=thisNode:      
                        thisNode.next=prev.right
                        thisNode=prev.right
                prev=prev.next
            thisNode=node
            while thisNode:
                if thisNode.left:
                    self.helper(thisNode.left,thisNode)
                    break
                if thisNode.right:
                    self.helper(thisNode.right,thisNode)
                    break
                thisNode=thisNode.next


n1=TreeLinkNode(1)
n2=TreeLinkNode(2)
n3=TreeLinkNode(3)
n4=TreeLinkNode(4)
n5=TreeLinkNode(5)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5

s=Solution()
s.connect(n1)