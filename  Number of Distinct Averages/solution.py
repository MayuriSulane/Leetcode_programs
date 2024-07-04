class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        average=[]
        while nums:
            minelem= min(nums)
            maxele= max(nums)
            avg=(minelem+maxele)/2.0
            nums.remove(minelem)
            nums.remove(maxele)
            
            if avg in average:
                continue
            else:
                average.append(avg)
        return len(average)