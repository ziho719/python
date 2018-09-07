import numpy as np
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return []
        if n==1:
            return [0,1]
        if n==2:
            return [0,1,3,2]
        res=[0,1,3,2]
        for i in range(2,n):
            temp=[j+2**i for j in res[::-1]]
            res+=temp
        return res
s=Solution
print(s.grayCode(s,1))
print(s.grayCode(s,2))
print(s.grayCode(s,3))
print(s.grayCode(s,4))



