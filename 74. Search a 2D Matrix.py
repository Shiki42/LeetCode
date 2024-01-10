class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def search_row(nums,t):
            
            l,r = 0, len(nums)-1
            while l < r:
                mid = (l+r)//2
                if nums[mid] <= t and nums[mid+1] > t:
                    return mid
                elif nums[mid] > t:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
            
        def search_col(nums,t):
            l,r = 0, len(nums)-1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == t:
                    return True
                elif nums[mid] > t:
                    r = mid - 1
                else:
                    l = mid + 1
            return False
        if len(matrix) > 1:
            rows = [i[0] for i in matrix]
            row = search_row(rows,target)
        else:
            row = 0
        return search_col(matrix[row],target)