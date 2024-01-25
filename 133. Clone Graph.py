"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return None
        newNode = Node(node.val,[])
        created = {newNode.val:newNode}
        visited = set()
        q = [node]
        while q:
            cur = q.pop()
            visited.add(cur)
            newCur = created[cur.val]

            for i in cur.neighbors:
                
                if i not in visited and i not in q:
                    q.append(i)
                if i.val not in created.keys():
                    created[i.val] = Node(i.val,[])
                newCur.neighbors.append(created[i.val])

        return newNode
                    