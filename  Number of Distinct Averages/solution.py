class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        average=[]
        for i in range(len(nums)//2):
            maxi=max(nums)
            mini=min(nums)
            avg=float(maxi+mini)/2
            if avg not in average:
                average.append(avg)
            nums.remove(maxi)
            nums.remove(mini)
        return len(average)
