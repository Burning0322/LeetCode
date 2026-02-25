class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            find = target - num

            if find in seen:
                return [seen[find],i]
            
            seen[num]=i
        
        return []

        