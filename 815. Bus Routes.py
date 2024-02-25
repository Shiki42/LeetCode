from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
      q = []
      deep_map = {source:1}
      routes = map(set, routes)
      if source == target:
        return 0
      for i in routes[::-1]:
        if source in i:
          for j in i:
            if j == target:
              return 1
            if j not in deep_map:
              deep_map[j] = 1
              q.append(j)
    
      while q:
        new = []
        while q:
          cur = q.pop()
          for i in routes[::-1]:
            if cur in i:
              for j in i:
                if j == target:
                  return deep_map[cur]+1
                if j not in deep_map:
                  deep_map[j] = deep_map[cur]+1
                  new.append(j)
              routes.remove(i)
        q = new
        
      return -1