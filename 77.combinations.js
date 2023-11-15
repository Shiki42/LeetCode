/*
 * @lc app=leetcode id=77 lang=javascript
 *
 * [77] Combinations
 */

// @lc code=start
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function (n, k) {
  function backtrack(start, cur) {
    if (cur.length === k) {
      res.push(cur);
      return;
    }
    for (let i = start; i <= n; i++) {
      if (k - cur.length <= n - i + 1) {
        backtrack(i + 1, [...cur, i]);
      }
    }
  }
  let res = [];
  backtrack(1, []);
  return res;
};
// @lc code=end
