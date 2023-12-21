class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, (num//2)+1
        while l<=r:
            mid = (l + r) // 2
            if mid**2 == num:
                return True
            elif mid**2 < num:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
