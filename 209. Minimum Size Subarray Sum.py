class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        win = 0
        l, r = 0, 0
        res = 0
        while r < len(nums):
            count += nums[r]
            r += 1
            win += 1
            
            while count >= target and l < r:
                res = min(res,win) if res != 0 else win
            
                count -= nums[l]
                l += 1
                win -= 1

        return res
                
            

