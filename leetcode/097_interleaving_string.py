class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.hash={} #哈希表牛逼
        if len(s1)+len(s2)!=len(s3):
            return False
        return self.help(s1,s2,s3)
    def help(self,s1,s2,s3):
        i1=0
        i2=0
        if (len(s1),len(s2)) in self.hash:
            return self.hash[(len(s1),len(s2))]
        if s1=='':
            return s2==s3
        elif s2=='':
            return s1==s3
        elif s3=='':
            return False

        for s in s3:
            if s1[i1]==s and s2[i2]==s:
                if self.help(s1[i1+1:],s2[i2:],s3[i1+i2+1:]):
                    self.hash[(len(s1),len(s2))]=True
                    return True
                elif self.help(s1[i1:],s2[i2+1:],s3[i1+i2+1:]):
                    self.hash[(len(s1),len(s2))]=True
                    return True
                self.hash[(len(s1),len(s2))]=False
                return False
            elif s1[i1]==s:
                i1+=1
            elif s2[i2]==s:
                i2+=1
            else:
                self.hash[(len(s1),len(s2))]=False
                return False
        
            if i1==len(s1):
                self.hash[(len(s1),len(s2))]=s2[i2:]==s3[i1+i2:]
                return s2[i2:]==s3[i1+i2:]
            elif i2==len(s2):
                self.hash[(len(s1),len(s2))]=s1[i1:]==s3[i1+i2:]
                return s1[i1:]==s3[i1+i2:]
            elif len(s3)==i1+i2:
                self.hash[(len(s1),len(s2))]=False
                return False


s=Solution()

print(s.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa","babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab","babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))