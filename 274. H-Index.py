class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        citations.reverse()
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i

        return len(citations)