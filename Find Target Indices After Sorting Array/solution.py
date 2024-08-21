class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r=[]
        for i,j in enumerate(sorted(nums)):
            if j == target:
                r.append(i)
        return r