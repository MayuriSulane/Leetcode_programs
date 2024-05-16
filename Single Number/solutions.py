class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        db=[]
        if len(nums) == 1:
            return nums[0]
        for i,n in enumerate(nums):
            if i < len(nums):
                if n in nums[i+1:] or n in db:
                    db.append(n)
                else:
                    return n
            elif n not in db:
                return n
            