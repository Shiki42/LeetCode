class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        memo = [1 for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i],memo[j]+1)

        for i in memo:
            res = max(i,res)            
        return res