class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        
        average=[]
        for i in range(len(nums)//2):
            minElement= min(nums)
            maxElement=max(nums)
            avg = float(minElement + maxElement) /2
            average.append(avg)
            nums.remove(minElement)
            nums.remove(maxElement)   
        return min(average)