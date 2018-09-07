class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        elif len(nums)==1:
            return TreeNode(nums[0])
        posi=int(len(nums)/2)
        root=TreeNode(nums[posi])
        root.left=self.sortedArrayToBST(nums[:posi])
        root.right=self.sortedArrayToBST(nums[posi+1:])
        return root