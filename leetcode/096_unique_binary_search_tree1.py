class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        self.hash={}       
        return self.helper(n)
        
    def helper(self,n):
        """
        type n: int  
        rtype:int 
        """
        res=0
        if n<2:
            return 1

        if n in self.hash:
            return self.hash[n]
               
        for i in range(n):
            
            left=self.helper(i)
            right=self.helper(n-1-i)
            res+=left*right
            
        self.hash[n]=res
        return res

s=Solution()
print(s.numTrees(4))