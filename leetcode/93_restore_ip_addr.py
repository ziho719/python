class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        start=0
        length=len(s)
        res=[]
        for a in [1,2,3]:
            if length-start-a>9 or length-start-a<3:
                continue
            if a==2 and s[start]=='0':
                continue
                
            if a==3 and ( s[start]=='0'  or int(s[start:start+3])>255):
                continue
            start+=a
            for b in [1,2,3]:
                if length-start-b>6 or length-start-b<2:
                    continue
                if b==2 and s[start]=='0':
                    continue
                if b==3 and ( s[start]=='0'  or int(s[start:start+3])>255):
                    continue
                start+=b
                for c in [1,2,3]:
                    if length-start-c>3 or length-start-c<1:
                        continue
                    if c==2 and s[start]=='0':
                        continue
                    if c==3 and ( s[start]=='0'  or int(s[start:start+3])>255):
                        continue
                    if length-start-c>1 and (s[start+c]=='0'  or int(s[start+c:length])>255):
                        continue
                    
                    res.append(s[0:a]+'.'+s[a:a+b]+'.'+s[a+b:a+b+c]+'.'+s[a+b+c:length])

                        
                    
                start-=b
            start-=a
        return res


s=Solution()
print(s.restoreIpAddresses("0000"))