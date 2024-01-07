class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorials,nums = [1],['1']
        for i in range(1,n):
            factorials.append(factorials[i - 1] * i)
            nums.append(str(i + 1))
        k -= 1
        
        # Compute the factorial representation of k
        output = []
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]
            output.append(nums[idx])
            del nums[idx]

        return ''.join(output)