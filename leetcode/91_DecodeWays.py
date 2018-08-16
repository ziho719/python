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
        if len(s)==0:
            return 0
        dp=[0 for i in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            if i!=0:
                continue
            else:
                if i==len(s)-1:
                    dp[i]=1
                elif s[i+1]=='0':
                    if '0'<s[i]<'3': 
                        if i+2==len(s):
                           dp[i]=1
                        else:
                            dp[i]=dp[i+2]
                    else:
                        #比如304 直接断的类型
                        dp[i]=0
                

                    
                        
                    

                    


s=Solution()
print(s.numDecodings("10"))
