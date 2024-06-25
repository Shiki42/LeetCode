"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """

        def find_parents(p):
          s = set()
          depth = 0
          
          while p != None:
            s.add((p,depth))
            p = p.parent
            depth -= 1
            
          return s,depth
        
        
        p_prt, p_depth = find_parents(p)
        q_prt, q_depth = find_parents(q)
        
        p_r = set()
        q_r = set()
        #统一两条node list的深度
        for i in p_prt:
          p_r.add((i[0],i[1] - p_depth))
        for j in q_prt:
          q_r.add((j[0],j[1] - q_depth))
          
        u = p_r & q_r
        s=[]
        
        for i in u:
          s.append(i)
        s.sort(key = lambda x : x[1])
        
        return s[-1][0]