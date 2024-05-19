class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vo=set('aeiouAEIOU')
        sa=list(s)
        l=0
        r=len(sa)-1

        while l<=r:
            if sa[l] in vo and sa[r] in vo:
                sa[r],sa[l]=sa[l],sa[r]
                l+=1
                r-=1
            elif sa[l] not in vo:
                l+=1
            elif sa[r] not in vo:
                r-=1
        return "".join(sa)