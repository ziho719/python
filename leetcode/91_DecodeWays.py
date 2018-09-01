class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #太慢了，要用dp
        # num=0
        # if s[0]=='0':
        #     return 0
        # if len(s)==1:
        #     return 1
        # elif len(s)==2:
        #     if s[0]=='1' and s[1]!='0':
        #         return 2
        #     elif s[0]=='2' and '0'<s[1]<'7':
        #         return 2
        #     elif s[0]>'2' and s[1]=='0':
        #         return 0
        #     else:
        #         return 1
        # else:
        #     if s[0]=='1':
        #         num+=self.numDecodings(s[2:])
        #     elif s[0]=='2' and s[1]<'7':
        #         num+=self.numDecodings(s[2:])
        #     num+=self.numDecodings(s[1:])
        # return num


        # if len(s)==0:
        #     return 0
        # dp=[0 for i in range(len(s))]
        # for i in range(len(s)-1,-1,-1):
        #     if s[i]=='0':
        #         continue
        #     else:
        #         if i==len(s)-1:
        #             dp[i]=1
        #         elif s[i+1]=='0':
        #             if '0'<s[i]<'3': 
        #                 if i+2==len(s):
        #                    dp[i]=1
        #                 else:
        #                     dp[i]=dp[i+2]
        #             else:
        #                 #比如304 直接断的类型
        #                 return 0
        #         elif s[i]=='1':
        #             if i+2==len(s):
        #                dp[i]=2
        #             else:
        #                 dp[i]=max(dp[i+2],dp[i+1])+1
        #         elif s[i]=='2' and s[i+1]<'7':
        #             if i+2==len(s):
        #                dp[i]=2
        #             else:
        #                 dp[i]=max(dp[i+2],dp[i+1])+1
        #         else:
        #             dp[i]=dp[i+1]

        # # for i in dp:
        # #     print(i )

        # return dp[0]
        
        #应该是自顶向下的dp,个屁
        
        #COOOOOOOOOOOOOOOL!!!!!!!!!!!!!!
        
        # def numDecodings(self, s):
        #     v, w, p = 0, int(s>''), ''
        #     for d in s:
        #         v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
        #     return w
        # w tells the number of ways
        # v tells the previous number of ways
        # d is the current digit
        # p is the previous digit

        v=0
        w=int(s>'')
        p=''
        for d in s:
             v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
        return w



s=Solution()
print(s.numDecodings("210231234951201"))
