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
        self.helper(root,None)
        
    def helper(self,node,node_next):
        if node is None:
            return
        
        node.next=node_next
        
        self.helper(node.left,node.right)
        
        right_next = node_next.left if node_next else None
        
        self.helper(node.right,right_next)
        