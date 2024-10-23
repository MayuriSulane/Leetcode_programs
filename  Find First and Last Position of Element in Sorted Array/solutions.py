class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        if target not in nums:
            return [-1,-1]

        res=[]
        for n,i in enumerate(nums):
            if target == i:
                res.append(n)

        if res:
            return [res[0],res[-1]]
        else:
            return [-1,-1]