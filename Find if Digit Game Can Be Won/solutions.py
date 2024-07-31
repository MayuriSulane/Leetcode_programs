class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res_si=0
        re_do=0
        for i in nums:
            if i<10:
                res_si= res_si + i
            if i >=10:
                re_do= re_do + i        
        if res_si > re_do or re_do > res_si:
            return True
        return False