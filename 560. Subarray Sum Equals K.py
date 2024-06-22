class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums == []:
          return 0
        if len(nums) < 2:
          if nums[0] == k:
            return 1
          else:
            return 0
        
        d = defaultdict(lambda : 0)
        d[0] = 1
        count, _sum = 0 , 0
        for i in range(len(nums)):
          _sum+=nums[i]
          if d.has_key(_sum - k):
            count += d[_sum - k]
          d[_sum] +=1
        return count