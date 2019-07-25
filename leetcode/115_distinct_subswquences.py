class Solution:
    # def __init__(self):
    #     self.hashmap={}
    # def numDistinct(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: int
    #     这个hash就是逊啦
    #     """
    #     num=0
    #     posi=0
    #     if (len(s),len(t)) in self.hashmap:
    #         return self.hashmap[(len(s),len(t))]
    #     if t=='':
    #         return 1
    #     elif s=='':
    #         return 0

    #     for char in s:
    #         if char==t[0]:
    #             temp=self.numDistinct(s[posi+1:],t[1:])
    #             self.hashmap[(len(s)-posi-1,len(t)-1)]=temp
    #             num+=temp
    #         posi+=1
    #     self.hashmap[(len(s),len(t))]=num
    #     return num
    #
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not t:
            return 1
        if not s:
            return 0

        dp=[[0 for i in range(len(t))] for j in range(len(s))]
        dp[0][0]=int(s[0]==t[0])

        for i in range(1,len(s)):
            dp[i][0]=int(s[i]==t[0])+dp[i-1][0]
        for i in range(1,len(t)):
            for j in range(i,len(s)):
                if s[j]==t[i]:
                    dp[j][i]=dp[j-1][i-1]+dp[j-1][i]
                else:
                    dp[j][i]=dp[j-1][i]
        return dp[-1][-1]

        

s=Solution()
print(s.numDistinct("rabbbits","rabbits"))