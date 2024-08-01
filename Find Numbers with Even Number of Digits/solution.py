class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        co=0
        for i in nums: 
            if len(str(i))%2 == 0:
                co= co+1   
            else:
                continue     
        return co