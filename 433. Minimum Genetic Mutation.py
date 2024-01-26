class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        if endGene not in bank:
            return -1
        def diff(s1,s2):
            cnt = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    cnt += 1
            
            return cnt == 1

        q = [(startGene,0)]
        visited = set()
        while q:
            cur,step = q.pop()
            if diff(cur,endGene):
                return step + 1
            for i in bank:
                if i != cur and i not in visited and diff(i,cur):
                    q.append((i,step+1))
                    visited.add(i)
        return -1