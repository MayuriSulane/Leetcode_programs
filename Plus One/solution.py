class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        return [int(k) for k in str(int(''.join(map(str, digits)))+1)]
