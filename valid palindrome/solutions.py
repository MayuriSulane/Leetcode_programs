class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t=str.lower(str(s))
        n="".join(ch for ch in t if ch.isalnum())
        st= "".join(reversed(n))
        if n == st:
            return True
        return False