class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def recur(grid,left,right,up,down):
            root = Node(False,False,None,None,None,None)
            if right == left:
                root.isLeaf = True
                root.val = grid[down][left]
                return root
            h_mid = (left + right) // 2
            print(h_mid)
            v_mid = (up + down) // 2
            root.bottomLeft = recur(grid,left,h_mid,up,v_mid + 1)
            root.bottomRight = recur(grid,h_mid+1,right,up,v_mid + 1)
            root.topLeft = recur(grid,left,h_mid,v_mid,down)            
            root.topRight = recur(grid,h_mid+1,right,v_mid,down)
            if root.bottomLeft.isLeaf and root.bottomRight.isLeaf and root.topLeft.isLeaf and root.topRight.isLeaf and \
                root.bottomLeft.val == root.bottomRight.val and root.bottomLeft.val == root.topLeft.val and \
                root.bottomLeft.val == root.topRight.val:
                root.isLeaf = True
                root.val = root.bottomLeft.val
                root.bottomLeft = None
                root.bottomRight = None
                root.topLeft = None
                root.topRight = None

            return root

        return recur(grid,0,len(grid)-1,len(grid)-1,0)