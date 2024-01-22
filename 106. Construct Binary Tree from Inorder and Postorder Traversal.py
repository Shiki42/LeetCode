class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        idx = {element : i for i,element in enumerate(inorder)}

        def build(in_left,in_right):
            if in_left > in_right:
                return None
            root = TreeNode(postorder.pop())
            index = idx[root.val]
            root.right = build(index+1, in_right)
            root.left = build(in_left, index-1)
            return root

        return build(0, len(inorder)-1)