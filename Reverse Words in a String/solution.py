class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip()
        ns=[]
        
        for i in s.split(" "):
            if len(i)>0:
                ns.append(i)
        
        v=' '.join(reversed(ns))
        
        return v