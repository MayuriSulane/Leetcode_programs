class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        r=[]
        e,o=0,0
        b=bin(n)[2:]
        re=b[::-1]
        for k,i in enumerate(re):
            if int(i) == 1:
                r.append(k)    
            if int(i)==0:
                continue
        for i in r:
            if (i % 2)== 0:
                e=e+1
            if (i%2) !=0:
                o=o+1
        return([e,o])