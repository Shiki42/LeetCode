/*
 * @lc app=leetcode id=105 lang=javascript
 *
 * [105] Construct Binary Tree from Preorder and Inorder Traversal
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
  if (preorder.length === 0) {
    return null;
  }
  let rootVal = preorder[0];
  let mid = inorder.indexOf(rootVal);

  let root = new TreeNode(
    rootVal,
    buildTree(preorder.slice(1, mid + 1), inorder.slice(0, mid)),
    buildTree(
      preorder.slice(mid + 1, preorder.length),
      inorder.slice(mid + 1, inorder.length)
    )
  );
  return root;
};
// @lc code=end
