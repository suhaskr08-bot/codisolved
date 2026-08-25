class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        j=1
        while(j<=101):
            if k*j not in nums:
                return k*j
            j+=1
        